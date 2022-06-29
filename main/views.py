from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from .models import Videos, UserAccount
from rest_framework.viewsets import ModelViewSet
from .serializers import VideoSerializer, UserAccountSerializer
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

class VideosViewSet(ModelViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self):
        if 'id' in self.request.query_params.keys():
            idd = int(self.request.query_params.get('id'))

            return Videos.objects.filter(pk=idd)

        if 'from' in self.request.query_params.keys() and 'to' in self.request.query_params.keys():
            fromm = int(self.request.query_params.get('from'))
            to = int(self.request.query_params.get('to'))

            return Videos.objects.filter(Q(pk__gte=fromm) & Q(pk__lte=to))

        amount = 0
        if 'amount' in self.request.query_params.keys():
            amount = int(self.request.query_params.get('amount'))

        amount = min(Videos.objects.count(), amount)

        return Videos.objects.all()[:amount]

class FindVideoSet(ModelViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self):
        if 'find' in self.request.query_params.keys():
            compare_string = str(self.request.query_params.get('find'))
            videos = Videos.objects.filter(name__contains=compare_string)

            if 'amount' in self.request.query_params.keys():
                amount = int(self.request.query_params.get('amount'))
                if amount < len(videos):
                    videos = videos[:amount]

            return videos

class GetUserSet(ModelViewSet):
    serializer_class = UserAccountSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.method == 'GET':
            if 'getme' in self.request.query_params.keys():
                user_data = UserAccount.objects.filter(account_id=self.request.user.id)
                if len(user_data) == 0:
                    UserAccount(account_id=self.request.user.id, nickname=self.request.user.username)

                    return UserAccount.objects.filter(account_id=self.request.user.id)
                else:
                    return user_data

        if self.request.method == 'POST':
            if 'nickname' in self.request.data.keys():
                UserAccount.objects.filter(account_id=self.request.user.id).update(nickname=self.request.data.get('nickname'))

            if 'description' in self.request.data.keys():
                UserAccount.objects.filter(account_id=self.request.user.id).update(description=self.request.data.get('description'))


# def get_video(request):
#     if request.method == 'POST' and request.FILES['video']:
#         vid = request.FILES['video']
#         fs = FileSystemStorage()
#
#     return JsonResponse({'detail': 'File is loading'})
