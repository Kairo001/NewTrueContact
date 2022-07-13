# DjangoRestFramework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# Serializers
from apps.campaigns.serializers import FormSerializer, FormFieldSerializer

class FormViewSet(viewsets.ModelViewSet):
  serializer_class = FormSerializer
  parser_classes = [JSONParser]

  def get_queryset(self, pk=None):
    if pk is None:
      return self.get_serializer().Meta.model.objects.filter(is_active=True)
    return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()

  def destroy(self, request, *args, **kwargs):
    """EndPoint to update the 'is_active' field to false."""
    instance = self.get_object()
    instance.is_active = False
    instance.save()
    return Response(status=status.HTTP_204_NO_CONTENT)