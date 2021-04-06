a = ["A", "B", "C", "D", "E"]
a.append("F")  # 리스트에 요소 새로 추가
a.insert(2, "b")  # 리스트의 해당 위치에 추가
a.extend(["G"])  # 리스트의 맨 뒤에 요소 추가
print(a)

print(a.count("C"))  # 리스트의 해당 요소의 개수를 돌려줌
print(a.index("D"))  # 리스트의 해당 요소의 위치를 돌려줌
a.remove("E")  # 리스트의 해당 요소를 제거
print(a)
b = [3, 1, 4, 5, 2]
b.sort()  # 리스트를 오름차순으로 정렬함
print(b)
b.reverse()  # 리스트를 내림차순으로 정렬함
# len() 리스트의 요소 개수를 구함
