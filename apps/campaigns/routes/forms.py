from rest_framework.routers import DefaultRouter
from apps.campaigns.views import FormViewSet

router = DefaultRouter()

router.register(r'forms', FormViewSet, basename = 'forms')

urlpatterns = router.urls