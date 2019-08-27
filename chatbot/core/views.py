import json
from django.http.response import HttpResponse
from django.views.generic import View
from django.conf import settings
from core.helpers.utlis import parse_and_send_fb_message
from core.helpers.message_processing import MessageProcessing
from core.tasks import book_suggest_bg_task

class FBWebHookView(View):

    def get(self, request, *args, **kwargs):
        hub_mode = request.GET.get('hub.mode')
        hub_token = request.GET.get('hub.verify_token')
        hub_challenge = request.GET.get('hub.challenge')
        if hub_token != settings.VERIFY_TOKEN:
            return HttpResponse('Error, invalid token', status_code=403)
        return HttpResponse(hub_challenge)

    def post(self, request, *args, **kwargs):
        customer_message = json.loads(request.body.decode('utf-8'))
        print(customer_message)
        for entry in customer_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    fb_user_id = message['sender']['id']
                    if message['message'].get('text'):
                        parse_and_send_fb_message(fb_user_id, message['message'])
        return HttpResponse("Success", status=200)

    def put(self, request, *args, **kwargs):
        # books = book_suggest_bg_task.delay(sender_id,23208863)
        return HttpResponse(books, status=200)
