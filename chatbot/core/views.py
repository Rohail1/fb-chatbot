import json
from django.http.response import HttpResponse
from django.views.generic import View
from django.conf import settings
from core.utlis import parse_and_send_fb_message
EXCLUDE_TEXT = ('Would You like to search books by title?',  "Would You like to search books by goodread's ID?")


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
