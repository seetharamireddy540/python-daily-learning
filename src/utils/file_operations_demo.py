import shutil
import os
import tempfile
import subprocess
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', 
                        level=logging.DEBUG,
                        filemode='a',
                        format='%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'

                        )
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    # Create file handler
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.info('Started')
    logger.info('Finished')
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

def setup_demo():
    """Create a demo directory structure for examples"""
    os.makedirs("demo/source", exist_ok=True)
    os.makedirs("demo/archive", exist_ok=True)

    with open("demo/source/README.md", "w") as f:
        f.write("# Hello World\n")
    with open("demo/source/README.org", "w") as f:
        f.write("#+TITLE: Hello World\n")
    with open("demo/source/README.rst", "w") as f:
        f.write("Hello World\n=========\n")
        f.write("\n")

    os.makedirs("demo/source/2021", exist_ok=True)
    with open("demo/source/2021/README.md", "w") as f:
        f.write("# Hello World 2021\n")

def cleanup_demo():
    """Remove the demo directory structure"""
    shutil.rmtree("demo", ignore_errors=True)

if __name__ == "__main__":
    main()