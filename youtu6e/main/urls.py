from .views import VideosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mainvideos', VideosViewSet, basename='Videos')

urlpatterns = router.urls