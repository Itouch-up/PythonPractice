a = 1
while a == 1:
    a = input("Data 입력 : ")
    a = a.split(" ")
    if a[0].isalpha() == 1 and a[1].isdigit() == True and a[2].isalnum():
        a[0] = a[0].upper()
        a[2] = a[2].capitalize()
        print(a)
    else:
        a = 1
