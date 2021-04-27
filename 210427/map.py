a = [1, 2, 3]
print(list(map(str, a)))


def nn(a):
    b = a*a
    return b


print(list(map(nn, [1, 2, 3, 4, 5])))
