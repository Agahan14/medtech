from rest_framework.views import APIView
from firebase_admin.messaging import Message, AndroidNotification, AndroidConfig, Notification
from fcm_django.models import FCMDevice
from rest_framework.response import Response
from handbook.models import Article
order_details = {
    'date_of_visit': '03/04/2021',
    'address': 'No 1, Ciroma Chukwuma Adekunle Street, Ikeja, Lagos'
}


#Notification for app


class FCMTest(APIView):
    def post(self, request):

        reg_id = request.data['reg_ids']
        FCMDevice.objects.create(registration_id=reg_id, type="android")
        article = Article.objects.first()
        message = Message(
            android=AndroidConfig(notification=AndroidNotification(title="Совет на неделю", body=f"{article.content}", sound="default"), )
        )
        FCMDevice.objects.last().send_message(message)

        return Response("Success?")
