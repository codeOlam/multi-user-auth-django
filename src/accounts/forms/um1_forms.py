from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import CustomUserModel, UserModel1


class UM1CreationForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
    	model 				= CustomUserModel
    	fields 				= ('email', 'is_usermodel1', 'password1', 'password2')



    def clean_password2(self):
    	# Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


    def clean_is_usermodel1(self):
    	is_usermodel1 = self.cleaned_data.get('is_usermodel1')
    	is_usermodel1=True
    	return is_usermodel1


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomeUserUpdateForm(UserChangeForm):
	password = ReadOnlyPasswordHashField()
	class Meta:
		model 				= CustomUserModel
		fields 				= ['username', 'first_name', 'last_name']


	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		return self.initial["password"]

class UM1ChangeForm(UserChangeForm):
	class Meta:
		model 				= UserModel1
		fields 				= ['exec_postion', 'level']