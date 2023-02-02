# задача написать функцию. Она принимает на вход число и возвращает следующее число, состоящее из этих же цифр.
# Если это невозможно вернуть изначальное число
# Примеры:
# 12 -> 21
# 21 -> 21
# 5037 -> 5073


def func(x):
    x2 = [int(b) for b in str(x)]  # перевод аргумента в список
    m = 0
    for i in sorted(x2, reverse=True):  # нахождение максимально возможного числа путём переворота списка(оптимизация)
        m = m * 10 + i
    for i in range(x + 1, m + 1):  # перебор чисел с преобразованием в списки
        y2 = [int(a) for a in str(i)]
        if sorted(x2) == sorted(y2):  # сравнение отсортированных списков
            return i
            exit(0)
    return x  # если не нашёл, возвращает то же число


g = int(input())
print(func(g))

# второй вариант

# def read_num(num: int) -> str:
#     s = str(abs(num))
#     a = s[::-1]
#     return a
#
#
# def get_num(num: str = "", start: int = 0) -> int:
#     if start == len(num) - 1:
#         return int(num[::-1])
#     cnt = 0
#     cut_num = num[:start]
#     result = num[::-1]
#     answer = ""
#
#     for i in range(start, len(num)):
#         if int(num[i]) < int(num[start]):
#             cnt = 1
#             cut_1 = "".join(sorted(list(tuple(num[start + 1: i + 1] + cut_num))))
#             cut_2 = num[i + 1:]
#             result = [cut_2[::-1], num[start], cut_1]
#             break
#
#     if cnt == 1 and start != len(num) - 1:
#         for i in result:
#             for num in i:
#                 answer += num
#         return int(answer)
#     return get_num(num, start + 1)


# объяснение, что я делал
# 1. беру последнее число и сравниваю со всеми
# 2, если находится число меньше чем последнее, то ставлю последнее на место меньшего, а от меньшего сортирую
# 3. склеиваю
