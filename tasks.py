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
def format(c):
    """Format code with black"""
    c.run("black src/ tests/ tasks.py")

@task
def lint(c):
    """Run mypy type checking"""
    c.run("mypy src/")

@task
def clean(c):
    """Clean build artifacts"""
    c.run("rm -rf build/ dist/ *.egg-info/ .mypy_cache/ .pytest_cache/")