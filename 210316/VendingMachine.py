print("사이다-700원 콜라-800원 물-1200원")
money = int(input("얼마를 입력하겠습니까 : "))
select = int(input("선택) 1-사이다 2-콜라 3-물 : "))
if select == 1 and money > 700:
    item = "사이다"
    charge = money-700
    print("사이다가 나왔습니다. 덜컹")
elif select == 2 and money > 800:
    item = "콜라"
    charge = money-800
    print("콜라가 나왔습니다. 덜컹")
elif select == 3 and money > 1200:
    item = "물"
    charge = money-1200
    print("물이 나왔습니다. 덜컹")
else:
    print("음료수를 뽑을 수 없습니다.")
    charge = money
print("잔돈", charge, "원 반환합니다.")
