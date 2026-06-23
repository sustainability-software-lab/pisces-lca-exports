.PHONY: test test-cov lint format

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=pisces_lca_exports --cov-report=term-missing

lint:
	ruff check src/ tests/

format:
	ruff format src/ tests/
