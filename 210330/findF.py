print("문서를 작성하세요")
doc = input("")
word = input("찾을 문자를 입력하세요 : ")
seq = 0
for i in range(doc.count(word)):
    if doc.count(word) > 0:
        seq = doc.find(word, seq)
        print(doc[seq], seq+1, "/", doc.count(word))
        seq += 1
