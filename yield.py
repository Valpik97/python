from time import sleep


def gen():
    yield 1
    yield 2
    yield 3

def pow_two(limit: int):
    i = 0
    while True:
        if 2 ** i > limit:
            return
        yield 2 ** i
        i += 1


for x in pow_two(10000):
    print(x)