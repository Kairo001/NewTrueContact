from rest_framework.routers import DefaultRouter
from apps.campaigns.views import FormViewSet, FormFieldViewSet

router = DefaultRouter()

router.register(r'forms', FormViewSet, basename = 'forms')
router.register(r'formfields', FormFieldViewSet, basename = 'formfields')

urlpatterns = router.urls