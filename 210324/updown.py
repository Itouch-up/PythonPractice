a = 50
n = 0
while n != a:
    n = int(input("예상 숫자를 입력하세요 : "))
    if n > a:
        print("down")
    elif n < a:
        print("up")
    else:
        print("정답")
