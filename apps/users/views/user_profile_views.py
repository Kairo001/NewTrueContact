# DjangoREstFramework
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# Serializers
from apps.users.serializers.user_profile_serializers import UserProfileSerializer, ListUserProfileSerializer

# Filters
from filters.mixins import FiltersMixin
from rest_framework import filters

# Models
from apps.users.models import DataProfile

class UserProfileViewSet(viewsets.ModelViewSet):
  serializer_class = UserProfileSerializer
  list_serializer_class = ListUserProfileSerializer
  filter_backends = [filters.SearchFilter, filters.OrderingFilter]
  parser_classes = [JSONParser, MultiPartParser]
  search_fields = ['first_name', 'last_name', 'document', 'data__data']
  ordering = ['first_name']

  def get_queryset(self, pk=None):
    if pk is None:
        return self.list_serializer_class.Meta.model.objects.filter(is_active=True)
    return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()

  @action(detail=True, methods=['get'])
  def data_user(self, request, pk=None):
    """EndPoint to get all the data of a user profile."""
    instance = self.get_object()
    data = instance.get_profile_data()
    return Response(data,status.HTTP_200_OK)

  @action(detail=True, methods=['get'])
  def number_contacts(self, request, pk=None):
    """EndPoint to get all the data of a user profile."""
    data = DataProfile.objects.filter(data=pk)
    users_profiles = []
    for fact in data:
      users_profiles.append(self.list_serializer_class.Meta.model.objects.get(id=fact.user_profile.id))
    serializer = self.list_serializer_class(users_profiles, many=True)
    return Response(serializer.data,status.HTTP_200_OK)

  def list(self, request, *args, **kwargs):
    """EndPoint to list all user profiles that are active."""
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