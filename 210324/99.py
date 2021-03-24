n = int(input("구구단 몇 단을 출력할까요 (종료를 원할 시 0을 입력해 주세요) : "))

while n != 0:
    i = 1
    if n == 0:
        break
    while i < 10:
        print(n*i)
        i += 1
    n = int(input("구구단 몇 단을 출력할까요 (종료를 원할 시 0을 입력해 주세요) : "))
