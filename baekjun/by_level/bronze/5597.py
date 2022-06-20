import sys
x = [0]*31
for i in range(28):
    x[i] = 1
print(x)
for i in range(1, 31):
    print(i)
    if not x[i]:
        print(i)