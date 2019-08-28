# fb-chatbot
Facebook Messenger Chatbot for bookstore pages.


# Setup Project
You need to take following steps to run the project on your machine.

1) clone the project and cd into it.
2) Run the following command

```shell script
./setup.sh
```
3) Rename .env.template to .env
4) Add the values of environment variables in the .env file.

# Run the Project

To run the project please use the following command

```shell script
python chatbot/manage.py runserver
```

# Tests

To the the test please use the following command

```shell script
coverage run chatbot/manage.py test core -v 2
```

To generate coverage report please run the following command

```shell script
coverage html
```

Coverage report can be found in the htmlcov folder. Simply open the 'index.html' into any browser to see the report.
