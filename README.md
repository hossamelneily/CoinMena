## Description
Implementing a service to get the exchange rate BTC/USD from Alphavantage API  

## Assumptions
1. use celery and redis broker to get the rate hourly

## Frameworks
1. django == 3.1.7

## Libraries 
1. requests
1. djangorestframework 
1. rest_framework_api_key
1. django-celery-results
1. django-celery-beat
1. redis
1. decouple


## Runtime Environment
1. python 3.9.2
1. docker
1. docker compose
1. environment variables: 
   * ALPHAVANTAGE_API_KEY
   * ALPHAVANTAGE_API_URL 
   * ALPHAVANTAGE_API_URL_FUNCTION
   * REDIS_URL


## setup Locally 
1. installing [poetry](https://python-poetry.org/docs/) to create virtual environment 
`pip install poetry`
1. Create new environment use  `poetry install ` with  in your project root where manage.py lives 
   

  > to make sure the VM is activated using `command+t` in case mac to open new tab
  >  
  The result in terminal should be something like:
   > (yourenv) Hossam@MyLab-2:~ hossam$
   
   

3. Run migrations: `python manage.py makemigrations` and `python manage.py migrate`
1. Run server: `python manage.py runserver`
1. Download redis 
   * using [Homebrew](http://brew.sh/) 
   > brew install redis
   > 
   > brew services start redis
   
   * Direct [Download](http://redis.io/download) 
1. open and test redis
   * open new Terminal
   * redis-cli ping
   > redis-cli ping
   > 
   > PONG
   * redis server
   > redis-server
1. Run Celery
   * Open a terminal window, Run Celery with in your project root where manage.py lives:
   > celery -A project.celery worker -l -B info
   
1. Download Postgres

##  setup using Docker

1. install docker and docker compose on your local PC (docker machine is optional)
1. Run `make services` in one shell, wait until all services are ready. There is also `make services-d` to run them in background.
1. Run `make image` to build fresh image of the app
1. Now you have couple of options
   1. Run `make tests` to run tests against that image
   1. Run `make dev-run` to run the image as a server and celery worker,
      open http://127.0.0.1:8000/admin/rest_framework_api_key/apikey/add/ to create API key to be able to access the API's
      open http://localhost:8000/api/v1/quotes (or your docker machine IP address) to play with it
      
   1. If there is a hanging container you can always run `make dev-down` and/or `make services-down`
   1. Run `make help` to get some extra help, read Makefile to see what is going on behind the scenes

## How to use
1. open http://127.0.0.1:8000/admin/rest_framework_api_key/apikey/add/
1. visit http://localhost:8000/api/v1/quotes/ to get latest rate from local DB
1. Using post method http://localhost:8000/api/v1/quotes/ to run celery task to get price from Alphavantage API.



