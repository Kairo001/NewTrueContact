from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewSet, UserProfileViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename = 'users')
router.register(r'user_profiles', UserProfileViewSet, basename='user_profiles')

urlpatterns2 = router.urls