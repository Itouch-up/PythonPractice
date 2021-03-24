a = [70, 70, 70, 70, 60, 59]
print("2020 제2회 한국사 시험 결과")
for i in range(len(a)):
    if a[i] >= 70:
        print(i+1, "번 학생은 1급 입니다.")
    elif a[i] >= 60:
        print(i+1, "번 학생은 2급 입니다.")
    else:
        print(i+1, "번 학생은 불합격 입니다.")
