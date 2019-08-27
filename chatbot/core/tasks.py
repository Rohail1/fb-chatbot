from celery import shared_task
from core.helpers.goodread import GoodReadService
from core.helpers.ibm_watson import NLPService
from core.helpers.messages import MESSAGES
from core.helpers.facebook import Facebook


@shared_task
def book_suggest_bg_task(sender_id, book_id):
    reviews = GoodReadService.get_reviews_by_book_id(book_id)
    scores = {
        'negative': 0,
        'positive': 0
    }
    for review in reviews:
        score = NLPService.get_sentiments(review.text)
        if score['sentiment']['document']['label'] == 'positive':
            scores['positive'] += 1
        elif score['sentiment']['document']['label'] == 'negative':
            scores['negative'] += 1

    print(scores)
    is_recommended = scores['positive'] >= scores['negative']
    response = MESSAGES.get('RECOMMAND_BOOK') if is_recommended else MESSAGES.get('NOT_RECOMMAND_BOOK')
    print(response)
    Facebook.send_message(sender_id, response)
