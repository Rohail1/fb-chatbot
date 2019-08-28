from core.helpers.messages import MESSAGES
from core.helpers.goodread import GoodReadService
from core.tasks import book_suggest_bg_task


class MessageProcessing:

    @staticmethod
    def is_greeting(message):
        greetings = message.get('nlp', {}).get('entities', {}).get('greetings', [])
        if len(greetings) < 1:
            return False
        else:
            return greetings[0].get('confidence', 0.0) > 0.7

    @staticmethod
    def handle_quick_reply(sender_id, message):
        payload_type = message.get('quick_reply', {}).get('payload')
        if payload_type == 'search.title':
            return MESSAGES.get('SEARCH_BY_TITLE')
        elif payload_type == 'search.id':
            return MESSAGES.get('SEARCH_BY_ID')
        elif 'id.' in payload_type:
            book_suggest_bg_task.delay(sender_id, payload_type.replace('id.', ''))
            return None
        else:
            return MESSAGES.get('GREETING')

    @staticmethod
    def is_goodread_id(message):
        goodread_id = message.get('text', '')
        return goodread_id.isdigit()

    @staticmethod
    def get_titles(message):
        quick_replies = []
        books = GoodReadService.search_book(message.get('text'))
        response_result = books['results']['work']
        max_length = 5 if len(response_result) > 5 else len(response_result)
        for value in range(0, max_length):
            quick_reply = {
                "content_type": "text",
                "title": response_result[value]['best_book']['title'],
                "payload": "id.%s" % response_result[value]['best_book']['id']['#text'],
                "image_url": response_result[value]['best_book']['image_url'],
            }
            quick_replies.append(quick_reply)
        return quick_replies
