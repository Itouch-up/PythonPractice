a = ""
print("문장을 입력해주세요. 'q'입력시 종료됩니다.")
while(a != 'q'):
    a = input("")
    print(a[0])
    for i in range(len(a)):
        if a[i] == " ":
            print(a[i+1])
