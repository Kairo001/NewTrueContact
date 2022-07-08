from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewSet, UserProfileViewSet, LabelViewSet, TypeViewSet, DataProfileViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename = 'users')
router.register(r'user_profiles', UserProfileViewSet, basename='user_profiles')
router.register(r'labels', LabelViewSet, basename='labels')
router.register(r'types', TypeViewSet, basename='types')
router.register(r'data_profile', LabelViewSet, basename='profil_data')


urlpatterns2 = router.urls