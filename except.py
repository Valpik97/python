def f(a, b):
    return a / b



try:
    a, b = [int(x) for x in input().split()]
    r1 = f(a, b)
    print(r1)
except ZeroDivisionError:
    print("Деление на 0")
except ValueError as error:
    print("Ошибка ввода: ", error)
else:
    print("Всё выполнилось успешно")
finally:
    print("Функция выполнилась")
