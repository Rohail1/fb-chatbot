class MessageProcessing:

    @staticmethod
    def is_greeting(message):
        greetings = message.get('nlp', {}).get('entities', {}).get('greetings', [])
        if len(greetings) < 1:
            return False
        else:
            return greetings[0].get('confidence', 0.0) > 0.7
