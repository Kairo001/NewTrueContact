"""Users app views."""

# Django
from django.urls import path

# Views to get and refresh the token.
from .views import CookieTokenObtainPairView, CookieTokenRefreshView, RetrieveUserView

urlpatterns = [
  path('auth/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('auth/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
  path('retriview/', RetrieveUserView.as_view(), name="retriview")
]