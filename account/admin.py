from django.contrib import admin
from .models import Profile, UserModel


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'image', 'email']
