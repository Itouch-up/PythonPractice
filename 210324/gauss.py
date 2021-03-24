n = int(input("(종료 '1') 숫자 입력 : "))
while n != 1:
    i = 0
    j = 0
    while j <= n:
        i += j
        j += 1
    print(i)
    n = int(input("(종료 '1') 숫자 입력 : "))
