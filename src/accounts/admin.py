from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserTypeA, UserTypeB, Users
from accounts.forms.uta_forms import UTACreationForm, UTAChangeForm, UserUpdateForm
# Register your models here.

class UsersAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserUpdateForm
    add_form = UTACreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_joined', 'is_admin', 'is_usertype_a', 'is_usertype_b')
    list_filter = ('is_admin', 'is_usertype_b', 'is_usertype_a')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff', 'is_usertype_a', 'is_usertype_b')}),
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


class UserTypeAAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = UTAChangeForm

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


class UserTypeBAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = UTAChangeForm

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
admin.site.register(Users, UsersAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
admin.site.register(UserTypeA, UserTypeAAdmin)
admin.site.register(UserTypeB, UserTypeBAdmin)
