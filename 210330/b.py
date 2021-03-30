
a = ""
print("문장을 입력해 주세요. 'q' 입력시 종료됩니다.\n")
while(a[0] != 'q'):
    a = input()
    if (a[-1] == "."):
        print("온점을 잘 입력하셨습니다.")
    else:
        print("온점을 입력해 주세요")
