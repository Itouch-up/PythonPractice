i = 0
fibo = 1
j = 1
while fibo < 100:
    print(fibo)
    fibo = i+j
    i = j
    j = fibo
