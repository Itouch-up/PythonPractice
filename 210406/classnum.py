student = ['이황', '이이', '원효']
print(student)
name = input("전학 온 학생은 누구입니까? ")
student.append(name)
print(student)
print("번호 재정렬....")
student.sort()
for i in range(len(student)):
    print("{0} {1}".format(i+1, student[i]))
