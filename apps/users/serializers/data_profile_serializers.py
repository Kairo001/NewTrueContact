# DjangoRestFramework 
from rest_framework import serializers

# Models
from apps.users.models import DataProfile, Type, Label

class LabelSerializer(serializers.ModelSerializer):

  class Meta:
    model = Label
    fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):

  class Meta:
    model = Type
    fields = '__all__'

class DataProfileSerializer(serializers.ModelSerializer):

  class Meta:
    model = DataProfile
    exclude = ['is_active', 'created_date', 'modified_date']