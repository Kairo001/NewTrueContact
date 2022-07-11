# RestFramework
from rest_framework import serializers

# User model
from django.contrib.auth import get_user_model
User = get_user_model()

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
      'user_permissions' : instance.user_permissions.all().values_list('name', flat=True)
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