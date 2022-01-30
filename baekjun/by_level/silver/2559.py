import sys

n, k = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))

init_s = [sum(temp[0:k])]

for i in range(n - k):
    init_s.append(init_s[-1]-temp[i]+temp[i+k])
print(max(init_s))