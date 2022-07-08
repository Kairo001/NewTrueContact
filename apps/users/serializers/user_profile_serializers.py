# DjangoRestFramework
from rest_framework import serializers

# UserProfile Model
from apps.users.models import UserProfile

class ListUserProfileSerializer(serializers.ModelSerializer):

  class Meta:
    model = UserProfile
    exclude = ['is_active', 'created_date', 'modified_data']

  def to_representation(self, instance):
    return {
      'first_name': instance.first_name,
      'last_name' : instance.last_name,
      'document' : instance.document,
      'image' : instance.image if instance.image != '' else ''
    }

class UserProfileSerializer(serializers.ModelSerializer):

  class Meta:
    model = UserProfile
    exclude = ['is_active', 'created_date', 'modified_data']
  
  def to_representation(self, instance):
    return {
      'first_name': instance.first_name,
      'last_name' : instance.last_name,
      'document' : instance.document,
      'image' : instance.image if instance.image != '' else '',
      'data' : instance.get_profile_data()
    }