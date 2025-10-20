# python-daily-learning

## Quick Start

```bash
# Install Poetry (if not installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Run invoke tasks
poetry run invoke install
poetry run invoke test
poetry run invoke format
poetry run invoke lint

# Docker
docker-compose up --build
```

## Poetry Commands

```bash
# Dependencies
poetry add requests         # Add production dependency
poetry add pytest --group dev  # Add dev dependency
poetry remove requests      # Remove dependency

# Environment
poetry shell               # Activate virtual environment
poetry run python app.py   # Run command in Poetry env

# Build & publish
poetry build               # Build package
poetry publish             # Publish to PyPI
```