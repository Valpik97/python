from typing import Callable, List, Any
import time


def logger(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        a: int = 0
        while func(*args, **kwargs):
            print(f"{a} seconds")
            a += 0.1
            time.sleep(0.1)

    return wrapper

@logger
def f(x: int) -> None:
    print(5 * x + 8)

f(5)