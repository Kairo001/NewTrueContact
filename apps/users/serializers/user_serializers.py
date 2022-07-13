# Django
from django.contrib.auth import authenticate

# RestFramework
from rest_framework import serializers

# User model
from django.contrib.auth import get_user_model
User = get_user_model()

class ListUserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    exclude = ['is_superuser', 'is_staff', 'last_login', 'is_active']

  def to_representation(self, instance):
    return {
      'id' : instance.id,
      'username' : instance.username,
      'full_name' : instance.get_full_name(),
      'first_name' : instance.first_name,
      'last_name' : instance.last_name,
      'image' : instance.image.url  if instance.image else ''
    }

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    exclude = ['is_superuser', 'is_staff', 'last_login', 'is_active']

  def to_representation(self, instance):
    return {
      'id' : instance.id,
      'username' : instance.username,
      'full_name' : instance.get_full_name(),
      'groups' : instance.groups.all().values_list('name', flat=True),
      'user_permissions' : instance.user_permissions.all().values_list('name', flat=True),
      'image' : instance.image.url if instance.image else ''
    }

class PasswordSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=128, min_length=8, write_only=True)
  confirm_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

  def validate(self, data):
    if data['password'] != data['confirm_password']:
      raise serializers.ValidationError(
        {'password':'Las contraseñas no coinciden.'}
      )
    return data

class UpdatePasswordSerializer(serializers.Serializer):
  current_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
  password = serializers.CharField(max_length=128, min_length=8, write_only=True)
  confirm_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

  def validate_current_password(self, value):
    user = authenticate(username=self.context['username'], password=value)
    if not user:
      raise serializers.ValidationError("La contraseña actual no es correcta.")
    
    return value

  def validate(self, data):
    if data['password'] != data['confirm_password']:
      raise serializers.ValidationError(
        {'password':'Las contraseñas no coinciden.'}
      )
    return data