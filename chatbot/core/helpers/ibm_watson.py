import json
from django.conf import settings
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions


class NLPService:

    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        iam_apikey=settings.WATSON_NLP_API_KEY,
        url=settings.WATSON_NLP_URL
    )

    @classmethod
    def get_sentiments(cls, review):
        response = cls.natural_language_understanding.analyze(
            text=review,
            features=Features(sentiment=SentimentOptions()),
            language='en',
        ).get_result()
        return response
