.PHONY: build up down restart web nuke-it-all

docker_compose = docker-compose -f docker-compose.yml

build:
	cp .env.development .env
	$(docker_compose) build

up:
	$(docker_compose) up

down:
	$(docker_compose) down

restart:
	$(MAKE) down
	$(MAKE) up

all:
	$(MAKE) build
	$(MAKE) up

nuke-it-all:
	$(docker_compose) down --volumes --remove-orphans
	docker system prune
	rm .env
