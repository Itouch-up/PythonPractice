def TodayMenu(*menu):
    print("오늘의 메뉴")
    for i in range(len(menu)):
        print(menu[i])
    print("Service Charge, VAT 10% will be added")


TodayMenu("만두", "김말이", "만두")
