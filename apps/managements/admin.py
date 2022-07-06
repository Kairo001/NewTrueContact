"""Enrollment of models so that they appeared in the Django admin panel."""

from django.contrib import admin

# Models
from apps.managements.models import TypeManagement, OriginManagement, Management, DataField

class TypeManagementAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id',)
  search_fields = ('id', 'name')
  list_per_page = 25

admin.site.register(TypeManagement, TypeManagementAdmin)

class OriginManagementAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'type')
  list_display_links = ('id',)
  search_fields = ('id', 'name', 'type')
  list_per_page = 25

admin.site.register(OriginManagement, OriginManagementAdmin)

class ManagementAdmin(admin.ModelAdmin):
  list_display = ('id', 'campaign', 'agent', 'client', 'status', 'origin')
  list_display_links = ('id',)
  search_fields = ('id', 'campaign', 'agent', 'client', 'status', 'origin')
  list_per_page = 25

admin.site.register(Management, ManagementAdmin)

class DataFieldAdmin(admin.ModelAdmin):
  list_display = ('id', 'management', 'form_field')
  list_display_links = ('id',)
  search_fields = ('id', 'management')
  list_per_page = 25

admin.site.register(DataField, DataFieldAdmin)