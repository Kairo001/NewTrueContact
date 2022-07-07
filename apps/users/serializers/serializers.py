# RestFramework
from rest_framework import serializers
from rest_framework.views import APIView

class TestUserSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=64)
  email = serializers.EmailField()

  # El orden de ejecución de los salierizadores es el siguiente:
  # - Ejecuta las funciones validate_<field> en donde <field> es el nombre del campo, esto tiene como objetivo validad un solo campo.
  # - Una vez ejecutado las funicones validate_<field> si es que existen, procede a ejecutar la función validate, la cual tiene como argumento de entrada todo los campos para así hacer la validación general.
  # 

  def validate_name(self, value):
    """Validación personalizada para name."""
    if 'albeiro' in value:
      raise serializers.ValidationError('No puede existir un usuario con este nombre.')

    return value

  def validate_email(self, value):
    """Validación personalizada para email."""
    if value == '':
      raise serializers.ValidationError('El campo email no puede estar vacío.')

    if self.validate_name(self.context['name']) in value:
      raise serializers.ValidationError('El email no puede contener el nombre.')

    return value

  def validate(self, data):
    # if data['name'] in data['email']:
    #   raise serializers.ValidationError('El email no puede contener el nombre.')
    return data

  def create(self, validated_data):
    return super().create(validated_data)

  def update(self, intance, validated_data):
    return super().update(validated_data)

  def save(self):
    return super().save()

  def to_representation(self, instance):
    return {
      'espacio' : instance.espacio
    }


class TestView(APIView):

  test_data = {
    'name' : 'albeiro001',
    'email' : 'albeiro01.98@gmail.com'
  }

  test_user = TestUserSerializer(data=test_data, context=test_data)