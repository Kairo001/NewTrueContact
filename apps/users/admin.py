"""Enrollment of models so that they appeared in the Django admin panel."""

from django.contrib import admin

# Modelos
from apps.users.models import UserProfile, Label, Type, DataProfile
from django.contrib.auth import get_user_model
User = get_user_model()

class UserAdmin(admin.ModelAdmin):
  list_display = ('username', 'user_profile', 'is_staff', 'is_superuser', 'last_login')
  list_display_links = ('username',)
  search_fields = ('username', 'is_staff', 'is_superuser')
  list_per_page = 25

admin.site.register(User, UserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name')
  list_display_links = ('id',)
  search_fields = ('id', 'first_name', 'last_name')
  list_per_page = 25

admin.site.register(UserProfile, UserProfileAdmin)

class LabelAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id',)
  search_fields = ('id', 'name')
  list_per_page = 25

admin.site.register(Label, LabelAdmin)

class TypeAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id',)
  search_fields = ('id', 'name')
  list_per_page = 25

admin.site.register(Type, TypeAdmin)

class DataProfileAdmin(admin.ModelAdmin):
  list_display = ('id', 'user_profile', 'type', 'label')
  list_display_links = ('id', 'user_profile')
  search_fields = ('id', 'user_profile', 'type', 'label')
  list_per_page = 25

admin.site.register(DataProfile, DataProfileAdmin)