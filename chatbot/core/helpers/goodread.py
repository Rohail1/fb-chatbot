import requests
import goodreads_api_client as gr
from django.conf import settings
from bs4 import BeautifulSoup


class GoodReadService:

    client = gr.Client(developer_key=settings.GOODREAD_API_KEY)

    @classmethod
    def get_book_by_id(cls, book_id):
        return cls.client.Book.show(book_id)

    @classmethod
    def search_book(cls, q, field='title'):
        books = cls.client.search_book(q, field)
        return books

    @classmethod
    def get_reviews_by_book_id(cls,book_id):
        book = cls.client.Book.show(book_id)
        review_widget = book['reviews_widget']
        review_holder = BeautifulSoup(review_widget, 'html.parser')
        review_url = review_holder.find('iframe')
        r = requests.get(review_url['src'])
        response_html = r.text
        review_page = BeautifulSoup(response_html, 'html.parser')
        all_div = review_page.findAll('div')
        reviews = []
        for div in all_div:
            if 'gr_review_text' in div.get('class', []):
                reviews.append(div)
        return reviews
