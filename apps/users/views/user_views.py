

# DjangoREstFramework
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# Serializers
from apps.users.serializers import UserSerializer, PasswordSerializer, ListUserSerializer, UpdatePasswordSerializer

# Filters
from filters.mixins import FiltersMixin
from rest_framework import filters

class UserViewSet(viewsets.ModelViewSet):
  list_serializer_class = ListUserSerializer
  serializer_class = UserSerializer
  parser_classes = [JSONParser, MultiPartParser]
  filter_backends = [filters.SearchFilter, filters.OrderingFilter]
  search_fields = ['first_name', 'last_name', 'username']
  ordering = ['username']

  def get_queryset(self, pk=None):
    if pk is None:
        return self.list_serializer_class.Meta.model.objects.filter(is_active=True)
    return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()

  @action(detail=True, methods=['put'])
  def update_password(self, request, pk=None):
    """Endpoint to update the user's password."""
    instance = self.get_object()
    update_password_serializer = UpdatePasswordSerializer(data=request.data, context={'username':instance.username})
    update_password_serializer.is_valid(raise_exception=True)
    instance.set_password(request.data['password'])
    instance.save()
    return Response(status.HTTP_200_OK)

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
      serializer = self.list_serializer_class(page, many=True)
      return self.get_paginated_response(serializer.data)

    serializer = self.list_serializer_class(queryset, many=True)
    return Response(serializer.data)

  def destroy(self, request, *args, **kwargs):
    """EndPoint to update the 'is_active' field to false."""
    instance = self.get_object()
    instance.is_active = False
    instance.save()
    return Response(status=status.HTTP_204_NO_CONTENT)