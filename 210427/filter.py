def num(a):
    return type(a) == int


a = [1, 'a', '가', 5, 9.99, -10]
print(filter(num, a))
print(list(filter(num, a)))
