def f(x):
    return 5 * x + 8


def transform(numbers):
    result = []
    for x in numbers:
        result.append(f(x))
    return result

def sum_numbers(a, b, *args, **kwargs):
    s=0
    print(args)
    print(kwargs)
    for key in kwargs:
        s+=kwargs[key]
    for x in args:
        s+=x
    return a+b+s


#data = [int(x) for x in input().split()]
#res = transform(data)
#print(res)


print(sum_numbers(1, 2, 3, 3, 3, 3, f=3, m=3, j=3))
