i = 1


def cafe(i):

    while(True):
        coffee = input('커피종류를 입력하세요 : ')
        if coffee == '마감':
            break
        name = input('고객명을 입력하세요 : ')
        if(name == ''):
            name = i
        print("%s 고객님, 주문하신 %s 나왔습니다." % (name, coffee))
        i += 1


cafe(i)
