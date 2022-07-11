

# DjangoREstFramework
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status

# Serializers
from apps.users.serializers import UserSerializer, PasswordSerializer

class UserViewSet(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  parser_classes = [JSONParser, MultiPartParser]

  def get_queryset(self, pk=None):
    if pk is None:
        return self.get_serializer().Meta.model.objects.filter(is_active=True)
    return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()

  def create(self, request, *args, **kwargs):
    password_serializer = PasswordSerializer(data=request.data)
    password_serializer.is_valid(raise_exception=True)
    user_serializer = self.get_serializer(data=request.data)
    user_serializer.is_valid(raise_exception=True)
    user_serializer.save()
    return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    
  def list(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    
    page = self.paginate_queryset(queryset)
    if page is not None:
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)