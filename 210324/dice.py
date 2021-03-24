from random import *
throw = 0
print("주사위 프로그램을 시작합니다. 첫번째 숫자는")
while throw != 'q':
    print(randint(1, 6))
    throw = input("아무기나 누르시면 주사위가 던져집니다. 종료를 원하시면 'q'를 입력하세요")
