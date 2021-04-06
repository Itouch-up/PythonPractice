while True:
    pwd = input("비밀번호를 입력해주세요 : ")
    if len(pwd) < 8:
        print("비밀번호는 8자리 이상입니다.")
    elif pwd.isalpha() == False:
        print("비밀번호는 영문자와 숫자의 조합입니다.")
    elif pwd.isdigit() == False:
        print("비밀번호는 영문자와 숫자의 조합입니다.")
    else:
        print("비밀번호는 {0}입니다.".format(pwd))
        break
