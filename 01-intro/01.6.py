file = open('file.txt', 'r') # Открываем файл на чтение
file.close()                 # Закрываем файл
print(file.closed)           # Выведет True


with open('file.txt', 'r') as file: # Открываем файл
  print(file.readlines())           # Что-то с ним делаем

print(file.closed)                  # Тут файл уже закрыт



# Можно считать файл целиком в одну строку с помощью метода read()
with open('file.txt', 'r') as file:
  content = file.read()
  print(content)

# Можно считать все строки в список с помощью метода readlines()
with open('file.txt', 'r') as file:
  content = file.readlines()
  print(content)

# Можно считывать файл по одной строчке с помощью метода readline()
with open('file.txt', 'r') as file:
  s = file.readline()
  print(s.upper())
  s2 = file.readline()
  print(s2.lower())

# В цикле для перебора строк достаточно перебрать файл
with open('file.txt', 'r') as file:
  for line in file:
    print(line.upper())


with open('file.txt', 'w') as file:
	# С помощью print(), указав специальный аргумент file
	print('Something great', file=file)
	
	# С помощью метода write(), если нужно записать одну строку
	file.write('Hello Earth!\n')
	
	# С помощью метода writelines(), если нужно записать список из строк
	file.writelines(['Hello\n', 'Goodbye'])