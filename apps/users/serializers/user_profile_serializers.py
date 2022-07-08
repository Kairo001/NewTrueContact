# DjangoRestFramework
from rest_framework import serializers

# UserProfile Model
from apps.users.models import UserProfile

class ListUserProfileSerializer(serializers.ModelSerializer):

  class Meta:
    model = UserProfile
    exclude = ['is_active', 'created_date', 'modified_date']

  def to_representation(self, instance):
    return {
      'id' : instance.id,
      'first_name': instance.first_name,
      'last_name' : instance.last_name,
      'document' : instance.document if instance.document else '',
      'image' : instance.image.url if instance.image else ''
    }

class UserProfileSerializer(serializers.ModelSerializer):

  class Meta:
    model = UserProfile
    exclude = ['is_active', 'created_date', 'modified_date']
  
  def to_representation(self, instance):
    return {
      'first_name': instance.first_name,
      'last_name' : instance.last_name,
      'document' : instance.document if instance.document else '',
      'image' : instance.image.url if instance.image else '',
      'data' : instance.get_profile_data()
    }

  def validate_document(self, value):
    if UserProfile.objects.filter(document=value, is_active=True).exists():
      raise serializers.ValidationError("Ya existe un contacto con este número de documento.")
    return value