import json
from django.test import SimpleTestCase
from collections import OrderedDict
from bs4.element import Tag
from celery.contrib.testing.worker import start_worker
from core import tasks
from core.helpers.goodread import GoodReadService
from core.helpers.message_processing import MessageProcessing


class GoodReadTest(SimpleTestCase):

    def test_get_book_by_id(self):
        book_id = 1128434
        book = GoodReadService.get_book_by_id(book_id)
        self.assertTrue(isinstance(book, OrderedDict))
        self.assertEqual(book['id'], '1128434')
        self.assertEqual(book['isbn'], '0575077832')
        self.assertEqual(book['title'], 'The Last Wish (The Witcher, #1)')

    def test_reviews_by_book_id(self):
        book_id = 1128434
        reviews = GoodReadService.get_reviews_by_book_id(book_id)
        self.assertTrue(isinstance(reviews, list))
        for review in reviews:
            self.assertTrue(isinstance(review, Tag))
            self.assertIn('gr_review_text', review['class'])

    def test_search_book(self):
        query = 'shadow hunter'
        books = GoodReadService.search_book(query)
        self.assertTrue(isinstance(books, OrderedDict))
        self.assertIn('query', books)
        self.assertIn(books['query'], query)
        self.assertIn('results', books)
        self.assertTrue(isinstance(books['results'], OrderedDict))
        self.assertIn('work', books['results'])
        self.assertTrue(isinstance(books['results']['work'], list))


class MessageProcessingTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.celery_worker = start_worker(app)
        cls.celery_worker.__enter__()


    def test_is_greeting(self):
        message = {
            'nlp': {
                'entities': {
                    'greetings': [
                        {
                            'confidence': 0.9
                        }
                    ]
                }
            }
        }
        is_greeting = MessageProcessing.is_greeting(message=message)
        self.assertTrue(is_greeting)
        message = {
            'nlp': {
                'entities': {
                    'greetings': [
                        {
                            'confidence': 0.2
                        }
                    ]
                }
            }
        }
        is_greeting = MessageProcessing.is_greeting(message=message)
        self.assertFalse(is_greeting)

    def test_is_goodread_id(self):
        message = {
            'text': '2453565'
        }
        is_goodread_id = MessageProcessing.is_goodread_id(message=message)
        self.assertTrue(is_goodread_id)
        message = {
            'text': '245Af3565'
        }
        is_goodread_id = MessageProcessing.is_goodread_id(message=message)
        self.assertFalse(is_goodread_id)

    def test_get_titles(self):
        message = {
            'text': 'Subtle Art'
        }
        replies = MessageProcessing.get_titles(message=message)
        self.assertTrue(isinstance(replies, list))

    def test_handle_quick_reply(self):
        sender_id = 235535445
        message = {
            'quick_reply': {
                'payload': 'search.title'
            }
        }
        response = MessageProcessing.handle_quick_reply(sender_id, message=message)
        self.assertTrue(isinstance(response, dict))
        self.assertIn('text', response)
        self.assertEqual(response['text'], 'Please enter the title of the book.')

        message = {
            'quick_reply': {
                'payload': 'search.id'
            }
        }
        response = MessageProcessing.handle_quick_reply(sender_id, message=message)
        self.assertTrue(isinstance(response, dict))
        self.assertIn('text', response)
        self.assertEqual(response['text'], "Please enter the goodread's ID.")
