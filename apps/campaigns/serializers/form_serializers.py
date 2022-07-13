# DjangoRestFramework
from rest_framework import serializers

# Models
from apps.campaigns.models import Form, FormField

class FormSerializer(serializers.ModelSerializer):

  class Meta:
    model = Form
    exclude = ['is_active', 'created_date', 'modified_date']

class FormFieldSerializer(serializers.ModelSerializer):

  class Meta:
    model = FormField
    exclude = ['is_active', 'created_date', 'modified_date']