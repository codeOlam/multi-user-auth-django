from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserModel1, UserModel2, CustomUserModel
from accounts.forms.um1_forms import UM1CreationForm, UM1ChangeForm, CustomeUserUpdateForm
# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = CustomeUserUpdateForm
    add_form = UM1CreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_joined', 'is_admin', 'is_usermodel1', 'is_usermodel2')
    list_filter = ('is_admin', 'is_usermodel2', 'is_usermodel1')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'slug')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff', 'is_usermodel1', 'is_usermodel2')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class UserModel1Admin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = UM1ChangeForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('exec_postion', 'level')
    list_filter = ('level',)
    fieldsets = (
        (None, {'fields': ('user', 'exec_postion', 'level')}),
    )

    search_fields = ('exec_postion',)
    ordering = ('level',)
    filter_horizontal = ()


class UserModel2Admin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = UM1ChangeForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('qualification', 'appointment')
    list_filter = ('appointment',)
    fieldsets = (
        (None, {'fields': ('user', 'qualification', 'appointment')}),
    )

    search_fields = ('qualification',)
    ordering = ('appointment',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(CustomUserModel, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
admin.site.register(UserModel1, UserModel1Admin)
admin.site.register(UserModel2, UserModel2Admin)
