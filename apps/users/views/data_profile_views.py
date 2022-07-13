# DjangoRestFramework
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action

# Serializers
from apps.users.serializers import LabelSerializer, TypeSerializer, DataProfileSerializer

class LabelViewSet(viewsets.ModelViewSet):
  pagination_class = None
  serializer_class = LabelSerializer
  parser_classes = [JSONParser]

  def get_queryset(self, pk=None):
    if pk is None:
      return self.get_serializer().Meta.model.objects.all()
    return self.get_serializer().Meta.model.objects.filter(id=pk).first()

class TypeViewSet(viewsets.ModelViewSet):
  pagination_class = None
  serializer_class = TypeSerializer
  parser_classes = [JSONParser]

  def get_queryset(self, pk=None):
    if pk is None:
        return self.get_serializer().Meta.model.objects.all()
    return self.get_serializer().Meta.model.objects.filter(id=pk).first()

  @action(detail=True, methods=['get'])
  def labels(self, request, pk=None):
    """EndPoint to get all labels of a type."""
    instance = self.get_object()
    data = instance.get_labels()
    return Response(data,status.HTTP_200_OK)

class DataProfileViewSet(viewsets.ModelViewSet):
  serializer_class = DataProfileSerializer
  parser_classes = [JSONParser]

  def get_queryset(self, pk=None):
    if pk is None:
        return self.get_serializer().Meta.model.objects.filter(is_active=True)
    return self.get_serializer().Meta.model.objects.filter(id=pk, is_actice=True).first()