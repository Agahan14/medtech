from rest_framework.views import APIView
from firebase_admin.messaging import Message, AndroidNotification, AndroidConfig, Notification
from fcm_django.models import FCMDevice
from rest_framework.response import Response
from handbook.models import Article


# Notification for app


class FCMTest(APIView):
    def post(self, request):
        reg_id = request.data['reg_ids']
        FCMDevice.objects.create(registration_id=reg_id, type="android")
        message = Message(
            android=AndroidConfig(notification=AndroidNotification(title="Совет на неделю",
                                                                   body="Пейте витамины, которые рекомендовал Вам Ваш врач.",
                                                                   sound="default"), )
        )
        FCMDevice.objects.last().send_message(message)
        return Response("Success?")
