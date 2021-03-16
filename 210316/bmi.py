name = input("이름을 입력하세요 : ")
height = int(input("키(cm)을 입력하세요 : "))
weight = int(input("몸무게(kg)를 입력하세요(소수점 제외) : "))
bmi = round(weight/(height/100)**2, 2)
print()
print(name, "님의 키는", height, "cm이고 몸무게는", weight, "kg입니다.")
print("BMI 지수는", bmi, "입니다.")
if bmi > 30:
    n = "고도비만"
elif bmi >= 25:
    n = "비만"
elif bmi >= 23:
    n = "과체중"
elif bmi >= 18.5:
    n = "정상"
else:
    n = "저체중"
print(n, "입니다.")
