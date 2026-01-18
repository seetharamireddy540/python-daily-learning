import logging
logging.basicConfig(level=logging.DEBUG)


def logger(func):
    def wrapper(*args, **kwargs):
        logging.debug(f"Exeucting {func.__name__} with {args} and {kwargs}")
        print(f"Executing {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(a, b):
    return a + b


if __name__ == "__main__":
    result = add(3, 5)
    print(f" result = {result}")
