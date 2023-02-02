from typing import Callable, List, Any
from time import sleep


class Repeater:
    def __init__(self, value: Any):
        self.value: Any = value

    def __iter__(self):
        return self

    def __next__(self) -> Any:
        return self.value


class Count:
    def __init__(self, start: int, end: int):
        self.start = start
        self.value: int = start
        self.end = end

    def __iter__(self):
        self.value = self.start
        return self

    def __next__(self) -> Any:
        if self.value == self.end:
            print("raising StopIteration")
            raise StopIteration
        self.value += 1
        return self.value


# data1 = [3, 4, 5, 6]
# data = Repeater(data1)
data = Count(5, 10)
for x in data:
    print(x)
    sleep(1)

data = Count(5, 10)
for x in data:
    print(x)
    sleep(1)

# iterator = iter(data)
# print(iterator)
#
# while True:
#     x = None
#     try:
#         x = next(iterator)
#     except StopIteration:
#         break
#     print(x)


