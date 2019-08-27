
MESSAGES = {
    'GREETING': {
        "text": "Hello, how would you like to search the books?",
        "quick_replies": [
            {
                "content_type": "text",
                "title": "By title",
                "payload": 'search.title',
            }, {
                "content_type": "text",
                "title": "By goodread's ID",
                "payload": "search.id",
            }
        ]
    },
    "SEARCH_BY_ID": {
        'text': "Please enter the goodread's ID."
    },
    "SEARCH_BY_TITLE": {
        'text': "Please enter the title of the book."
    },
    "REPLY_TO_TITLE": {
      "text": "Following are the search result. Please a select a book."
    },
    "RECOMMAND_BOOK": {
        "text": "After going through the reviews, You should definetly get this book most of the readers "
                "enjoyed reading it."
    },
    "NOT_RECOMMAND_BOOK": {
        "text": "After going through the reviews, I suggest not to buy this book as it has negative reviews "
                "and the readers did not enjoy reading it."
    }
}