IMAGE_NAME = coinmena

all: image

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

image:         ## Build the docker image
	docker build -t $(IMAGE_NAME)  .

services:      ## Creates necessary services for development
	docker-compose -f ./docker/docker-compose.services.yml up --force-recreate

services-d:    ## Creates necessary services for development in background
	docker-compose -f ./docker/docker-compose.services.yml up -d

services-down:      ## Creates necessary services for development
	docker-compose -f ./docker/docker-compose.services.yml down

dev-run:       ## Run app locally
	docker-compose -f ./docker/docker-compose.yml up --force-recreate


dev-down:      ## Tear down app 
	docker-compose -f ./docker/docker-compose.yml down

test:          ## Run tests
	docker-compose -f ./docker/docker-compose.yml run server test



