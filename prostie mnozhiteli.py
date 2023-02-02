def smnozh(value: int):
    i = 2
    while True:
        if value % i == 0:
            value /= i
            yield i
        i += 1

for x in smnozh(2133):
    print(x)