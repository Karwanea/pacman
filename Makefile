PYTHON = python3
VENV = .venv
VENV_PYTHON = $(VENV)/bin/python



all: run

run: install

debug: install

clean:
	@echo "petit coup de propre"
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores \
		--ignore-missing-imports --disallow-untyped-defs \
		--check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict
