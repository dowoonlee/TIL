import sys

a, b = map(int, sys.stdin.readline().split())


seq = [0]
idx = 1
for i in range(1, 46):
    for j in range(i):
        seq.append(i)
        idx += 1
print(sum(seq[a:b+1]))

