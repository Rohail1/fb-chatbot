from core.helpers.facebook import Facebook
from core.helpers.message_processing import MessageProcessing


quick_replies = [
    {
        "content_type": "text",
        "title": "Red",
        "payload": 'red.txt',
        "image_url": "http://example.com/img/red.png"
    }, {
        "content_type": "text",
        "title": "Green",
        "payload": "ok",
        "image_url": "http://example.com/img/green.png"
    }
]


def parse_and_send_fb_message(sender_id, recevied_message):

    # tokens = re.sub(r"[^a-zA-Z0-9\s]", ' ', recevied_message.get('text')).lower()
    if recevied_message.get('quick_reply'):
        Facebook.send_message(sender_id, {'text': "response of quick reply"})
    else:
        if MessageProcessing.is_greeting(recevied_message):
            Facebook.send_message(sender_id, {'text': "hello man", "quick_replies": quick_replies})
        else:
            Facebook.send_message(sender_id, {'text': "no hello"})



