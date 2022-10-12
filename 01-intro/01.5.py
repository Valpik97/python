def get_sum(x, y):
	print(f"{x} + {y} = {x + y}")

get_sum(5, 7)  # Выведется "5 + 7 = 12"
get_sum(9, 15) # Выведется "9 + 15 = 24"

def get_sum(x, y):
	print(f"{x} + {y} = {x + y}")
	return x + y

s1 = get_sum(5, 7)  # Выведется "5 + 7 = 12"
s2 = get_sum(9, 15) # Выведется "9 + 15 = 24"

print(s1, s2)       # Выведется "12 24"


def get_sum(x, y=0):
	print(f"{x} + {y} = {x + y}")

get_sum(5, 7) # Выведется "5 + 7 = 12"
get_sum(9)    # Выведется "9 + 0 = 9"

print(int('5'))             # Выведется число 5
print(int('ABCD', base=16)) # Выведется число 43981
print(float('3.14'))        # Выведется число 3.14
print(bool(0))              # Выведется False

print(list(range(3)))       # Выведется [0, 1, 2]
print(tuple(range(3)))      # Выведется (0, 1, 2)
print(str(99))              # Выведется строка "99"
print(set(range(5)))        # Выведется {0, 1, 2, 3, 4}

x = 87

print(bin(x)) # 0b1010111
print(oct(x)) # 0o127
print(hex(x)) # 0x57

print(abs(-7))       # Модуль числа, 7
print(divmod(7, 3))  # Частное и остаток, (2, 1)
print(max(5, 7, 3))  # Максимум из набора, 7
print(min(1, 9, -7)) # Минимум из набора, -7
print(pow(3, 4))     # Возведение в степень, 3^4 = 81
print(round(1.41))   # Округление до ближайшего целого, 1

def filter_func(x):
	return x > 5

def map_func(x):
	return 2 * x

numbers = [5, 3, 10, 4, -1, 7, 11, 6]
another = {5, 3, 9, 2, 7, 3}

print(len(numbers)) # Длина коллекции
print(all(numbers)) # Все значения аналогичны True
print(any(numbers)) # Хотя бы одно значение аналогично True

# Функции ниже обёрнуты в list(), чтобы можно было вывести результат

# Создаёт кортежи с номерами элементов и самими элементами
# [(0, 5), (1, 3), (2, 10), (3, 4), (4, -1), (5, 7), (6, 11), (7, 6)]
print(list(enumerate(numbers)))

# Оставляет только те значения, для которых функция вернула True
# [10, 7, 11, 6]
print(list(filter(filter_func, numbers)))

# Преобразовывает значения с помощью заданной функции
# [10, 6, 20, 8, -2, 14, 22, 12]
print(list(map(map_func, numbers)))

# Разворачивает коллекцию
# [6, 11, 7, -1, 4, 10, 3, 5]
print(list(reversed(numbers)))

# Сортирует коллекцию
# [-1, 3, 4, 5, 6, 7, 10, 11]
print(list(sorted(numbers)))

# Склеивает две коллекции в одну в кортежи, пока одна из них не кончится
# [(5, 2), (3, 3), (10, 5), (4, 7), (-1, 9)]
print(list(zip(numbers, another)))