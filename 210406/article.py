win = input("승리팀 : ")
defeat = input("패배팀 : ")
score = input("스코어 : ")
match = int(input("경기유형(1,2,3) : "))
mvp = input("MVP 선수 이름 : ")
if match == 1:
    match = "불꽃튀는"
elif match == 2:
    match = "단조로운"
else:
    match = "일방적인"
print("오늘 {0}팀과 {1}팀의 경기가 있었습니다. 경기는 {0}팀의 {2} 승리로 끝이 났습니다. 오늘 승부는 {3} 경기가 펼쳐졌는데요. 양팀 다 더욱 더 분발하여 앞으로 더 좋은 경기력을 보여주겠다는 다짐을 내비쳤습니다. 오늘의 MVP는 {4} 선수였습니다. 요즘 {4} 선수의 기세가 만만치 않은데요. 이 상승세가 어디까지 이어질지 귀추가 주목됩니다.".format(win, defeat, score, match, mvp))
