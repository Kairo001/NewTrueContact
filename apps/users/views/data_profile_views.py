# DjangoRestFramework
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

# Serializers
from apps.users.serializers import LabelSerializer, TypeSerializer, DataProfileSerializer

class LabelViewSet(viewsets.ModelViewSet):
  serializer_class = LabelSerializer
  parser_classes = [JSONParser]

  def get_queryset(self, pk=None):
    if pk is None:
      return self.get_serializer().Meta.model.objects.all()
    return self.get_serializer().Meta.model.objects.filter(id=pk).first()

class TypeViewSet(viewsets.ModelViewSet):
  serializer_class = TypeSerializer
  parser_classes = [JSONParser]

  def get_queryset(self, pk=None):
    if pk is None:
        return self.get_serializer().Meta.model.objects.all()
    return self.get_serializer().Meta.model.objects.filter(id=pk).first()

class DataProfileViewSet(viewsets.ModelViewSet):
  serializer_class = DataProfileSerializer
  parser_classes = [JSONParser]

  def get_queryset(self, pk=None):
    if pk is None:
        return self.get_serializer().Meta.model.objects.all()
    return self.get_serializer().Meta.model.objects.filter(id=pk).first()