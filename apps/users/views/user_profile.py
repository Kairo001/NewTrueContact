# DjangoREstFramework
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

# Serializers
from apps.users.serializers.user_profile_serializers import UserProfileSerializer 

class UserProfileViewSet(viewsets.ModelViewSet):
  serializer_class = UserProfileSerializer
  parser_classes = [JSONParser]

  def get_queryset(self, pk=None):
    if pk is None:
        return self.get_serializer().Meta.model.objects.filter(is_active=True)
    return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()
    
  def list(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())

    page = self.paginate_queryset(queryset)
    if page is not None:
      serializer = self.get_serializer(page, many=True)
      return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)