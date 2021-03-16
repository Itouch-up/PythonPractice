r = float(input("원의 반지름을 입력하세요(cm) : "))
rod = round(2*3.14*r, 2)
area = round(3.14*(r**2), 2)
print("원의 둘레는", rod, "cm이고 원의 넓이는", area, "cm^2 입니다")
