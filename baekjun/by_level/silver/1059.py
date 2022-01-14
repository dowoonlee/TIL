import sys

l = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
s.sort()

if n in s:
    print(0)
else:
    st, ed = 1, 1
    for i in range(l):
        if s[i]<n:
            st = s[i] + 1
        else:
            ed = s[i]-1
            break

    print((n-st)*(ed-n+1) + ed - n)