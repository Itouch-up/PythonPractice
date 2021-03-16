n = int(input("자연수를 입력하여 주세요 : "))
if n <= 0:
    print("자연수가 아닙니다")
elif n % 2 == 0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")
