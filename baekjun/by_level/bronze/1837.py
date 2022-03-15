import sys

p, k = map(int, sys.stdin.readline().split())

flag = True
for i in range(2, k):
    if not(p%i):
        flag=False
        ans = i
        break
if flag:
    print("GOOD")
else:
    print("BAD", ans)