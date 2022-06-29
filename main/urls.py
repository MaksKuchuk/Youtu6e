from django.urls import path, re_path, include

from .views import VideosViewSet, FindVideoSet, GetUserSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mainvideos', VideosViewSet, basename='Videos')
router.register('findvideos', FindVideoSet, basename='FoundVideos')
router.register('userinfo', GetUserSet, basename='GetUserSet')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + router.urls