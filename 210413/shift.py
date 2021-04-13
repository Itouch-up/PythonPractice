def shift(*name):
    worker = len(name)
    print("교대 근무자의 수는 %d명입니다. 순서대로" % (worker))
    for a in name:
        print(a)


shift("홍길동", "이이", "신사임당")
