from youtu6e import settings
from .views import VideosViewSet, FindVideoSet
from rest_framework import routers

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register('mainvideos', VideosViewSet, basename='Videos')
router.register('findvideos', FindVideoSet, basename='FoundVideos')

urlpatterns = router.urls