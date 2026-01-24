import logging
logging.basicConfig(level=logging.DEBUG)


def logger(func):
    def wrapper(*args, **kwargs):
        logging.debug(f"Exeucting {func.__name__} with {args} and {kwargs}")
        print(f"Executing {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(a: int, b: int) -> int:
    return a + b


class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")


if __name__ == "__main__":
    # result = add(3, 5)
    # print(f" result = {result}")

    with MyContextManager() as cm:
        print("In context")
