.PHONY: mm merge m build run stop destroy destroy-hard rebuild armageddon clean cbr test t prompt b b-root sp shell pip db sql djlint mypy setup tasks revoke defender flush python-makemigrations python-makemigrations-merge migrate mmm backend-build r python-bash python-bash-root python-shell-plus python-pip-install python-db-shell python-shell-plus-sql lint docs scan db-rebuild seed create-chain arango arango-start arango-stop arango-logs

DOCKER_COMPOSE = COMPOSE_BAKE=true docker compose -f docker-compose.local.yml
DJANGO = $(DOCKER_COMPOSE) run --rm django
PYTHON = $(DJANGO) python
PIP_INSTALL = $(DJANGO) pip install -r requirements/local.txt

################
# core / build #
################

python-makemigrations:
	@echo "Running makemigrations..."
	$(PYTHON) manage.py makemigrations
mm: python-makemigrations

python-makemigrations-merge:
	@echo "Running makemigrations with merge..."
	$(PYTHON) manage.py makemigrations --merge
merge: python-makemigrations-merge

migrate:
	@echo "Running migrations..."
	$(PYTHON) manage.py migrate
m: migrate

mmm:
	@echo "Running makemigrations & migrate..."
	$(PYTHON) manage.py makemigrations && $(PYTHON) manage.py migrate

backend-build:
	@echo "Building backend..."
	$(DOCKER_COMPOSE) build

build: backend-build migrate
	@echo "Build completed."

run:
	@echo "Starting services..."
	$(DOCKER_COMPOSE) up

stop:
	@echo "Stopping services..."
	$(DOCKER_COMPOSE) down

destroy:
	@echo "Destroying containers and networks..."
	$(DOCKER_COMPOSE) down -v

destroy-hard: stop destroy
	@echo "Force removing containers and volumes..."
	$(DOCKER_COMPOSE) rm -v
	docker rm -f $(docker ps -a -q)
	docker volume rm $(docker volume ls -q)

rebuild: destroy build
	@echo "Rebuilding the application..."
r: rebuild

armageddon:
	@echo "Cleaning up all Docker artifacts..."
	docker stop $$(docker ps -a -q)
	docker rm $$(docker ps -a -q)
	docker network prune -f
	docker rmi -f $$(docker images --filter dangling=true -qa)
	docker volume rm $$(docker volume ls --filter dangling=true -q)
	docker rmi -f $$(docker images -a -q)
	docker system prune -a

clean: destroy stop
	@echo "Performing system-wide Docker cleanup..."
	docker system prune -af
	@echo "Removing debug files..."
	find debug/ -mindepth 1 -not -name .gitkeep -delete

cbr: clean build run
	@echo "Cleaned, built, and running."

flush:
	@echo "Flushing database..."
	$(PYTHON) manage.py flush
	@echo "Uninstalling GitHub Apps..."
	$(PYTHON) manage.py runscript uninstall_gh_apps


db-rebuild:
	@echo "Stopping and removing postgres service and associated volumes..."
	$(DOCKER_COMPOSE) rm -svf postgres
	@echo "Starting postgres service..."
	$(DOCKER_COMPOSE) up -d postgres
	@echo "Postgres service rebuilt."

###############
# development #
###############

seed:
	@echo "Seeding essential data (superuser, subscription plans, onboarding tasks)..."
	$(PYTHON) manage.py seed_data

test:
	@echo "Running tests..."
	$(PYTHON) -m pytest
t: test

test-prompt:
	@echo "Running prompt tests..."
	$(PYTHON) -m pytest -m "prompts"
prompt: test-prompt

python-bash:
	@echo "Starting bash shell in Django container..."
	$(DOCKER_COMPOSE) run --rm django bash
b: python-bash

python-bash-root:
	@echo "Starting bash shell as root in Django container..."
	$(DOCKER_COMPOSE) run --rm --user root django bash
b-root: python-bash-root

python-shell-plus:
	@echo "Starting Django shell_plus..."
	$(PYTHON) manage.py shell_plus
sp shell: python-shell-plus

python-pip-install:
	@echo "Installing Python packages..."
	$(PIP_INSTALL)
pip: python-pip-install

python-db-shell:
	@echo "Starting database shell..."
	$(PYTHON) manage.py dbshell
db: python-db-shell

python-shell-plus-sql:
	@echo "Starting Django shell_plus with SQL output..."
	$(PYTHON) manage.py shell_plus --print-sql
sql: python-shell-plus-sql

djlint:
	@echo "Linting Django templates..."
	djlint wraithscan/* --extension=html --reformat

lint:
	@echo "Linting Django files..."
	$(PIP_INSTALL)
	pre-commit run --all-files

mypy:
	@echo "Running MyPy for type checking..."
	mypy wraithscan/

docs:
	@echo "Generating documentation..."
	$(PYTHON) manage.py generate_swagger swagger.json

setup:
	@echo "Running setup script..."
	$(PYTHON) manage.py runscript setup_local

###########
# scripts #
###########
tasks:
	@echo "Setting up periodic tasks..."
	$(PYTHON) manage.py setup_periodic_tasks

revoke:
	@echo "Revoking tasks..."
	$(PYTHON) manage.py revoke_tasks

websocket:
	@echo "Running websocket test..."
	$(PYTHON) manage.py runscript test_websocket
