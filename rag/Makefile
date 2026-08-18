.PHONY: venv install freeze start stop test lint

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(PYTHON) -m pip
UVICORN := $(PYTHON) -m uvicorn
PYTEST := $(PYTHON) -m pytest
FLAKE8 := $(VENV)/bin/flake8

env:
	python3 -m venv $(VENV)

#clean the old virtual environment if it exists
# deactivate || true - run this in terminal to deactivate the virtual environment if it is active
deactivate:
	@echo "Deactivating virtual environment..."	
	rm -rf $(VENV)
	@echo "Virtual environment deactivated."

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

freeze:
	$(PIP) freeze > requirements.txt

run_vector_db:
	docker compose up

ollama_install:
	curl -fsSL https://ollama.com/install.sh | sh
	ollama list
	ollama pull smollm2:135m

ollama_run:
	ollama run smollm2:135m

ingest:
	$(PYTHON) ingest.py

query:
	$(PYTHON) query.py

test:
	$(PYTEST) -q

lint:
	ruff format .
	ruff check . --fix