a = (1, 2, 3, 4, 5, 4, 3, 2, 1)
print(a.count)
print(a.index)
pack = 1, 2, 3, 4, 5, 4, 3, 2, 1
b, c, *d = pack
print("b는 %d, c는 %d" % (b, c), "d는", d)
b, c = c, b
print("b는 %d, c는 %d" % (b, c))
