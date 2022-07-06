
#RestFramework
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# SimpleJWT
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

# TokenRefreshSelializer
from apps.users.serializers import CookieTokenRefreshSerializer

# User serializer
from apps.users.serializers import UserSerializer

class CookieTokenObtainPairView(TokenObtainPairView):
  """
  This view inherits from TokenObteinPairView so that the token is not included in the response but is stored in the cookies of the person who made the request with the "httonly" argument for greater security."""
  def finalize_response(self, request, response, *args, **kwargs):
    if response.data.get('refresh'):
      cookie_max_age = 3600 * 24 * 14 # 14 days
      response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True )
      del response.data['refresh']
    return super().finalize_response(request, response, *args, **kwargs)

class CookieTokenRefreshView(TokenRefreshView):
  """
  This view uses the 'refresh-token' variable stored in the cookies in order to return a new 'access-token'. If 'ROTATE_REFRESH_TOKENS' is true, the new 'refresh-token' is saved again in the cookies.
  """
  serializer_class = CookieTokenRefreshSerializer
  def finalize_response(self, request, response, *args, **kwargs):
    if response.data.get('refresh'):
      cookie_max_age = 3600 * 24 * 14 # 14 days
      response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True )
      del response.data['refresh']
    return super().finalize_response(request, response, *args, **kwargs)

class LogOut(APIView):
  """
  This view removes 'refresh-token' from cookies and also adds this same token to the blacklist so that it cannot be used.
  """
  permission_classes = [permissions.IsAuthenticated]
  def post(self, request):
    refresh_token = request.COOKIES.get('refresh_token')
    try:
      token = RefreshToken(refresh_token)
      token.blacklist()

      response = Response()
      response.delete_cookie(key='refresh_token')
      response.status_code = status.HTTP_205_RESET_CONTENT
      return response
    except Exception as e:
      return Response(status=status.HTTP_400_BAD_REQUEST)

class RetrieveUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = request.user
    user = UserSerializer(user)

    return Response(user.data, status=status.HTTP_200_OK)