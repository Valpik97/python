from typing import Callable, List


def operator(operation: str) -> Callable[[int], int]:
    def get_product(a: int, b: int) -> int:
        return a * b

    def get_sum(a: int, b: int) -> int:
        return a + b

    if operation == "+":
        return get_sum
    elif operation == "*":
        return get_product
    else:
        raise ValueError(f"wrong operation {operation}")


def f(x) -> int:
    return 7 ** x - 9


numbers: List = [3, -2, -7, 6, 4, 0, -5]
numbers.sort(key=lambda x: x ** 2)
print(*numbers)

# Callable[[тип параметра], тип возвращаемого значения]
another_f: Callable[[int], int] = f

numbers.sort(key=another_f)
print(*numbers)

print(operator("*")(5, 8))

# 1)Функция - объект
# 2)Функции могут принимать другие функции
# 2.2)Функции могут фозрващать другие функии
# 3)Функции можно вкладывать друг в друга
