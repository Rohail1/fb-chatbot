from core.helpers.facebook import Facebook
from core.helpers.message_processing import MessageProcessing
from core.helpers.messages import MESSAGES


def parse_and_send_fb_message(sender_id, recevied_message):

    if recevied_message.get('quick_reply'):
        respose_msg = MessageProcessing.handle_quick_reply(recevied_message)
        Facebook.send_message(sender_id, respose_msg)
    else:
        if MessageProcessing.is_greeting(recevied_message):
            Facebook.send_message(sender_id, MESSAGES.get('GREETING'))
        elif MessageProcessing.is_goodread_id(recevied_message):
            Facebook.send_message(sender_id, {'text': "Suggest buy or not"})
        else:
            Facebook.send_message(sender_id, {'text': "Return Titles"})



