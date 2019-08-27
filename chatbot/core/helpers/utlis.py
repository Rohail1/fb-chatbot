from copy import deepcopy
from core.helpers.facebook import Facebook
from core.helpers.message_processing import MessageProcessing
from core.helpers.messages import MESSAGES
from core.tasks import book_suggest_bg_task


def parse_and_send_fb_message(sender_id, recevied_message):

    Facebook.send_action(sender_id)
    if recevied_message.get('quick_reply'):
        respose_msg = MessageProcessing.handle_quick_reply(sender_id,recevied_message)
        if respose_msg:
            Facebook.send_message(sender_id, respose_msg)
    else:
        if MessageProcessing.is_greeting(recevied_message):
            Facebook.send_message(sender_id, MESSAGES.get('GREETING'))
        elif MessageProcessing.is_goodread_id(recevied_message):
            book_suggest_bg_task.delay(sender_id, recevied_message.get('text'))
        else:
            replies = MessageProcessing.get_titles(message=recevied_message)
            response = deepcopy(MESSAGES['REPLY_TO_TITLE'])
            response['quick_replies'] = replies
            Facebook.send_message(sender_id, response)



