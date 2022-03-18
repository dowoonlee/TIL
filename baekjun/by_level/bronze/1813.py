import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
cnt = [0]*(max(a)+1)

for i in a:
    cnt[i]+=1

ans = -1
for i, v in enumerate(cnt):
    if i==v:
        ans = i
print(ans)


