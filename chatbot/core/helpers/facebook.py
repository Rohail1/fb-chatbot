import json
import requests
from django.conf import settings


class Facebook:
    FB_ENDPOINT = settings.FB_ENDPOINT
    PAGE_ACCESS_TOKEN = settings.PAGE_ACCESS_TOKEN

    @classmethod
    def send_request_fb(cls, payload):
        endpoint = f"{cls.FB_ENDPOINT}/me/messages?access_token={cls.PAGE_ACCESS_TOKEN}"
        request_payload = json.dumps(payload)
        response = requests.post(endpoint, headers={"Content-Type": "application/json"}, data=request_payload)
        return response.json()

    @classmethod
    def send_action(cls, fb_id, action='typing_on'):
        payload = {
            "recipient": {
                'id': fb_id
            },
            "sender_action": action
        }
        return cls.send_request_fb(payload)

    @classmethod
    def send_message(cls, fb_id, message):
        payload = {
            "recipient": {
                'id': fb_id
            },
            "message": message
        }
        return cls.send_request_fb(payload)
