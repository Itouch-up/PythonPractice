a = ["123", "456", "789"]
print(type(a[0]), type(a[1]), type(a[2]))

a = list(map(int, a))
print(type(a[0]), type(a[1]), type(a[2]))

print(list(map(lambda x: x*10, (3, 5, 7, 9))))
