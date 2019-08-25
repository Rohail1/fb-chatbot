from core.helpers.messages import MESSAGES


class MessageProcessing:

    @staticmethod
    def is_greeting(message):
        greetings = message.get('nlp', {}).get('entities', {}).get('greetings', [])
        if len(greetings) < 1:
            return False
        else:
            return greetings[0].get('confidence', 0.0) > 0.7

    @staticmethod
    def handle_quick_reply(message):
        payload_type = message.get('quick_reply', {}).get('payload')
        if payload_type == 'search.title':
            return MESSAGES.get('SEARCH_BY_TITLE')
        elif payload_type == 'search.id':
            return MESSAGES.get('SEARCH_BY_ID')
        else:
            return MESSAGES.get('GREETING')

    @staticmethod
    def is_goodread_id(message):
        goodread_id = message.get('text', '')
        return goodread_id.isdigit()
