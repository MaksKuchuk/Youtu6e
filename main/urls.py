from .views import VideosViewSet, FindVideoSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mainvideos', VideosViewSet, basename='Videos')
router.register('findvideos', FindVideoSet, basename='FoundVideos')

urlpatterns = router.urls