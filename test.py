a = [1, 2, 3, 4]
b = [4, 3, 2, 1]
c = sorted(a)
d = sorted(b)
print(c, d)
print(sorted(a) == sorted(b))


print(sorted(a, reverse=True))

# перевод из числа в список
x2 = [int(s) for s in str(a)]

# перевод из списка в число
res = 0
for i in b:
  res = res * 10 + i
print(res)