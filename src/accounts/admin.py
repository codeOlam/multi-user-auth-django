from django.contrib import admin

from .models import UserModel1, UserModel2, CustomUserModel
# Register your models here.


admin.site.register(CustomUserModel)
admin.site.register(UserModel1)
admin.site.register(UserModel2)
