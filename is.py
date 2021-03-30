print("문장을 입력하세요 q 입력시 종료 합니다.")
a = ""
while a != 'q':
    a = input("")
    spa = 1
    for i in range(len(a)):
        if a[i] == " ":
            spa += 1
    if a == "q":
        break
    else:
        print("이 문장은", spa, "어절 입니다.")
