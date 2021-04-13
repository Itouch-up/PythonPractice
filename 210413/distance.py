def distance(x=0, y=0):
    if x == 0 and y == 0:
        x = int(input("x좌표를 입력하세요 : "))
        y = int(input("y좌표를 입력하세요 : "))
    c = (x**2+y**2)**0.5
    return c


print(distance())
