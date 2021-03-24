hp = 100
while hp > 0:
    print("주인공의 체력은", hp, "입니다.")
    attack = int(input("얼마의 데미지를 입히시겠습니까 : "))
    hp -= attack
print("주인공이 죽었습니다.")
