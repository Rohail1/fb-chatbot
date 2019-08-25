
MESSAGES = {
    'GREETING': {
        "text": "Hello, how would you like to search the books?",
        "quick_replies" : [
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
    }
}