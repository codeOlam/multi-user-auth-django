from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import Users, UserTypeA


class UTACreationForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
    	model 				= Users
    	fields 				= ('email', 'is_usertype_a', 'password1', 'password2')



    def clean_password2(self):
    	# Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


    def clean_is_usertype_a(self):
    	is_usertype_a = self.cleaned_data.get('is_usertype_a')
    	is_usertype_a=True
    	return is_usertype_a


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(UserChangeForm):
	password = ReadOnlyPasswordHashField()
	class Meta:
		model 				= Users
		fields 				= ['username', 'first_name', 'last_name']


	# def clean_password(self):
	# 	# Regardless of what the user provides, return the initial value.
	# 	return self.initial["password"]

class UTAChangeForm(UserChangeForm):
	class Meta:
		model 				= UserTypeA
		fields 				= ['exec_postion', 'level']