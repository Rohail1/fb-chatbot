import json
from django.test import SimpleTestCase
from core.helpers.goodread import GoodReadService
from collections import OrderedDict
from bs4.element import Tag


class GoodReadTest(SimpleTestCase):

    def test_get_book_by_id(self):
        book = GoodReadService.get_book_by_id(1128434)
        self.assertTrue(isinstance(book, OrderedDict))
        self.assertEqual(book['id'], '1128434')
        self.assertEqual(book['isbn'], '0575077832')
        self.assertEqual(book['title'], 'The Last Wish (The Witcher, #1)')

    def test_reviews_by_book_id(self):
        reviews = GoodReadService.get_reviews_by_book_id(1128434)
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



