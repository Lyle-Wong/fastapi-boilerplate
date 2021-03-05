.PHONY: build-pex
.DEFAULT_GOAL : build-pex
CONTAINER = app
PORTS = -p 5001:5000
VOLUMES = -v $$(pwd):/app
DOCKER_RUN = docker run -e PEX_SCRIPT=gunicorn --rm -it $(VOLUMES) $(PORTS) $(CONTAINER)

build:  ## Build Docker container
	docker build -t $(CONTAINER) .

clean:
	rm -rf dist *.egg-info htmlcov

cleanCache:
	rm -rf .pytest_cache .venv

resolve:
	poetry install

install:
	pex -vvv . -o dist/app-$$(date +"%Y%m%d%H%M%S").pex --venv prepend --compile -c gunicorn --validate-entry-point --use-system-time

docker-compose:
	docker-compose up --build --remove-orphans -d
	docker cp app:/app dist/

test:
	poetry run pytest --cov-report=html