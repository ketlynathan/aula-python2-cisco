.PHONY: run test lint clean
run:
python main.py


test:
pytest -q


lint:
black --check . || true
flake8 || true


clean:
rm -rf dist build .pytest_cache __pycache__