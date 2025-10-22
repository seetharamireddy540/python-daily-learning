from invoke import task

@task
def install(c):
    """Install dependencies"""
    c.run("poetry install")

@task
def test(c):
    """Run tests"""
    c.run("pytest tests/")

@task
def coverage(c):
    """Run tests with coverage"""
    c.run("pytest --cov=src --cov-report=html --cov-report=term")

@task
def format(c):
    """Format code with black and isort"""
    c.run("isort src/ tests/ tasks.py")
    c.run("black src/ tests/ tasks.py")

@task
def lint(c):
    """Run all linting tools"""
    c.run("flake8 src/ tests/")
    c.run("mypy src/")

@task
def clean(c):
    """Clean build artifacts"""
    c.run("rm -rf build/ dist/ *.egg-info/ .mypy_cache/ .pytest_cache/ htmlcov/ .coverage")