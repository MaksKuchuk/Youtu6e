from rest_framework.serializers import ModelSerializer

from .models import Videos

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Videos
        fields = ['id', 'name', 'description', 'views', 'likes', 'dislikes', 'uploadtime', 'preview', 'video']