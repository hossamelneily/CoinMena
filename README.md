## Description
Implementing a service to check a Github repository is popular or not by using Github REST API 

## Assumptions
1. use celery and redis broker to Asyc the API requests 
1. Use third part package django-health-check for project health check, I tried to use google/Cadvisor
but got error `Failed to create a Container Manager: could not detect clock speed from output` and took time to solve 

## Frameworks
1. django == 3.1.7
1. pytest == 6.2.2

## Libraries 
1. requests
1. djangorestframework
1. django-celery-results
1. django-celery-beat
1. redis
1. django-health-check 

## Runtime Environment
1. python 3.9.2
1. docker
1. docker compose
1. environment variables: 
   * GITHUB_API_URL
   * GITHUB_API_USERNAME 
   * GITHUB_API_PASSWORD
   * REDIS_URL
   * SOFT_TIME_LIMIT


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
   > celery -A project.celery worker -l info
1. run test
   > pytest tests
   

##  setup using Docker

1. install docker and docker compose on your local PC (docker machine is optional)
1. Run `make services` in one shell, wait until all services are ready. There is also `make services-d` to run them in background.
1. Run `make image` to build fresh image of the app
1. Now you have couple of options
   1. Run `make tests` to run tests against that image
   1. Run `make dev-run` to run the image as a server and celery worker, open http://localhost:8000 (or your docker machine IP address) to play with it
   1. If there is a hanging container you can always run `make dev-down` and/or `make services-down`
   1. Run `make help` to get some extra help, read Makefile to see what is going on behind the scenes

## How to use
1. visit http://localhost:8000/api/check 
1. enter owner and repo_name to the check if repo is popular or not 
1. visit http://127.0.0.1:8000/ht/ for health check 


## Helpers
check if repo is popular or not depending on number of stars and number of forks
* `check_repos_popularity`
## API Reference


[Checker API](https://documenter.getpostman.com/view/12150062/Tz5wWESL#6c0ea98d-94d2-44ba-9bef-2542a1b931dd)


[Health Check API](https://documenter.getpostman.com/view/12150062/Tz5wWESL#e3d332a3-c8bd-4497-a9d1-47403f346d81)

## My Improvements if I have time:
1. manipulate more with the github API for example: check if the repo is forked or not 
1. build a frontend interface

