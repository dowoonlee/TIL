import sys
#n = int(sys.stdin.readline())
n = 29

d0 = len(str(n))

st = max([0, n - d0*9])

ans = []

for i in range(st, n-1, 1):
    d = len(str(i))
    t = i
    for j in range(d):
        t += int(str(i)[j])
    if t==n:
        ans.append(i)

if len(ans)==0:
    print(0)
else:
    print(min(ans))