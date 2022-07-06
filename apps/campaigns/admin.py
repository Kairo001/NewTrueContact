from django.contrib import admin

# Models
from apps.campaigns.models import Form, FormField, Campaign

class FormAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id',)
  search_fields = ('id', 'name')
  list_per_page = 25

admin.site.register(Form, FormAdmin)

class FormFieldAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'form', 'type')
  list_display_links = ('id',)
  search_fields = ('id', 'name', 'form', 'type')
  list_per_page = 25

admin.site.register(FormField, FormFieldAdmin)

class CampaignAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id',)
  search_fields = ('id', 'name')
  list_per_page = 25

admin.site.register(Campaign, CampaignAdmin)