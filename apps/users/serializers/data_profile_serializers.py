# DjangoRestFramework 
from rest_framework import serializers

# Models
from apps.users.models import UserProfile, DataProfile, Type, Label

class LabelSerializer(serializers.ModelSerializer):

  class Meta:
    model = Label
    fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):

  class Meta:
    model = Type
    fields = '__all__'

  def to_representation(self, instance):
    return {
      "id" : instance.id,
      "name" : instance.name
    }

class DataProfileSerializer(serializers.ModelSerializer):

  class Meta:
    model = DataProfile
    exclude = ['is_active', 'created_date', 'modified_date']