
#RestFramework
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# SimpleJWT
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

# TokenRefreshSelializer
from apps.users.serializers import CookieTokenRefreshSerializer

# User serializer
from apps.users.serializers import UserSerializer

class CookieTokenObtainPairView(TokenObtainPairView):
  def finalize_response(self, request, response, *args, **kwargs):
    if response.data.get('refresh'):
      cookie_max_age = 3600 * 24 * 14 # 14 days
      response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True )
      del response.data['refresh']
    return super().finalize_response(request, response, *args, **kwargs)

class CookieTokenRefreshView(TokenRefreshView):
  serializer_class = CookieTokenRefreshSerializer
  def finalize_response(self, request, response, *args, **kwargs):
    if response.data.get('refresh'):
      cookie_max_age = 3600 * 24 * 14 # 14 days
      response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True )
      del response.data['refresh']
    return super().finalize_response(request, response, *args, **kwargs)

class RetrieveUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = request.user
    user = UserSerializer(user)

    return Response(user.data, status=status.HTTP_200_OK)