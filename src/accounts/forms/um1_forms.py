from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUserModel, UserModel1


class UM1CreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model 				= CustomUserModel
		fields 				= ('username', 'email', 'password1', 'password2')



class CustomeUserUpdateForm(UserChangeForm):
	class Meta(UserChangeForm):
		model 				= CustomUserModel
		fields 				= ['email', 'username', 'first_name', 'last_name']

class UM1ChangeForm(UserChangeForm):
	class Meta(UserChangeForm):
		model 				= UserModel1
		fields 				= ['exec_postion', 'level']