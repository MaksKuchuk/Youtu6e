from django.contrib.auth.decorators import permission_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Videos, UserAccount
from rest_framework.viewsets import ModelViewSet
from .serializers import VideoSerializer, UserAccountSerializer
from django.db.models import Q, F
from django.core.files.storage import FileSystemStorage

class VideosViewSet(ModelViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self):
        if 'neid' in self.request.query_params.keys():
            idd = int(self.request.query_params.get('neid'))

            return Videos.objects.filter(~Q(pk=idd))

        if 'id' in self.request.query_params.keys():
            idd = int(self.request.query_params.get('id'))
            Videos.objects.filter(pk=idd).update(views=F('views') + 1)

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

class UserInfoAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if 'getme' in request.GET.keys():
            user_data = UserAccount.objects.filter(account_id=request.user.id)
            if user_data.count() == 0:
                UserAccount.objects.create(account_id=request.user.id, nickname=request.user.username)

                return Response(UserAccountSerializer(UserAccount.objects.filter(account_id=request.user.id), many=True).data)
            else:

                return Response(UserAccountSerializer(user_data, many=True).data)

    def post(self, request):
        user_id = request.user.id

        if 'nickname' in request.data.keys():
            UserAccount.objects.filter(account_id=user_id).update(nickname=request.data['nickname'])

        if 'description' in request.data.keys():
            UserAccount.objects.filter(account_id=user_id).update(description=request.data['description'])

        if 'avatar' in request.data.keys():
            UserAccount.objects.filter(account_id=user_id).update(avatar=request.data['avatar'])

        if 'header' in request.data.keys():
            UserAccount.objects.filter(account_id=user_id).update(header=request.data['header'])

        return Response({'detail': 'success'})



# def get_video(request):
#     if request.method == 'POST' and request.FILES['video']:
#         vid = request.FILES['video']
#         fs = FileSystemStorage()
#
#     return JsonResponse({'detail': 'File is loading'})
