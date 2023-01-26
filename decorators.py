from typing import Callable, List, Any


def f(x):
    return x // 2 + 7 ** x


def logger(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("Start function")
        func(*args, **kwargs)
        print("End function")

    return wrapper


@logger
def greet(name: str) -> None:
    print(f"Hello {name}")


greet('nick')
greet('money')
