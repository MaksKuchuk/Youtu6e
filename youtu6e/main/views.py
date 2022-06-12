from django.http import JsonResponse
from .models import Videos
from rest_framework.viewsets import ModelViewSet
from .serializers import VideoSerializer
from django.db.models import Q

class VideosViewSet(ModelViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self):
        if 'from' in self.request.query_params.keys() and 'to' in self.request.query_params.keys():
            fromm = int(self.request.query_params.get('from'))
            to = int(self.request.query_params.get('to'))

            return Videos.objects.filter(Q(pk__gte=fromm) & Q(pk__lte=to))

        amount = 0
        if 'amount' in self.request.query_params.keys():
            amount = int(self.request.query_params.get('amount'))

        amount = min(Videos.objects.count(), amount)

        return Videos.objects.all()[:amount]





