from django.urls import path, re_path, include

from .views import VideosViewSet, FindVideoSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mainvideos', VideosViewSet, basename='Videos')
router.register('findvideos', FindVideoSet, basename='FoundVideos')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + router.urls