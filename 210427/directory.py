import pickle
import os
print(os.getcwd())
print(os.listdir())

a = {1: 'a', 2: 'b', 3: 'C'}
b = [1, 2, 3, 4, 5]
with open('picklefile.bin', 'wb')as f:
    pickle.dump(a, f)
    pickle.dump(b, f)

with open('picklefile.bin', 'rb')as f:
    data = pickle.load(f)
    print(data)
