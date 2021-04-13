def sayhello(name, place="파이썬 월드"):
    print("%s님 안녕하세요 %s에 오신 것을 환영합니다." % (name, place))
    return name


user = sayhello('john')

user = sayhello('john', '프로그래밍 월드')
