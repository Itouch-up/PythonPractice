var = int(input("성적평균 : "))
if var >= 90:
    grade = "A"
elif var >= 80:
    grade = "B"
else:
    grade = "C"

print("이번 학기 성적은 ", grade, " 입니다.")
