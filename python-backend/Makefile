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

start:
	@echo "Starting server..."
	@$(UVICORN) main:app --host 127.0.0.1 --port 8000
	@echo "Server started with PID $$(cat .pid)"

stop:
	@if [ -f .pid ]; then \
		kill $$(cat .pid) 2>/dev/null || true; \
		rm -f .pid; \
		echo "Server stopped"; \
	else \
		echo "No server running"; \
	fi

test:
	$(PYTEST) -q

lint:
	$(FLAKE8) src