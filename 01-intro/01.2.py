print(5 > 3)   # Выведется True
print(4 >= 4)  # Выведется True
print(2 < 0)   # Выведется False
print(-3 <= 3) # Выведется True
print(7 == 8)  # Выведется False
print(6 != 1)  # Выведется True


a = 9
b = 3

print(a > b and b > 0) # True and True -> True
print(a < 3 or 9 == b) # False or False -> False
print(not a < b)       # not False -> True

x = int(input()) # Введём 9

if x < 5:        # Условие ложно, выполним ветку else
	print(2 * x)
else:


points = int(input('Баллы за семестр: ')) # Введём 75

if points > 90:                           # Условие ложно, проверим следующее
	print('Отлично (A)')
elif points > 83:                         # Условие ложно, проверим следующее
	print('Хорошо (B)')
elif points > 74:                         # Условие верное, поэтому...
	print('Хорошо (C)')                     # ... выводится "Хорошо (C)"
elif points > 67:
	print('Удовлетворительно (D)')
elif points >= 60:
	print('Удовлетворительно (E)')
else:
	print('Неудовлетворительно (FX)')	print(x + 9)   # Выведем 18


x = float(input())             # Вводим 8
y = x ** 2 if x < 5 else 5 * x # 8 больше 5, поэтому в y окажется 8 * 5 = 40
print(y)                       # Выведется 40