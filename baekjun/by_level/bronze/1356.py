import sys

n = str(sys.stdin.readline().rstrip())
nlist = [int(i) for i in n]

ans = False
for i in range(1, len(nlist)):
    a, b = nlist[0:i], nlist[i:]
    ax, bx = 1, 1
    for j in a:
        ax *= j
    for k in b:
        bx *= k
    if ax == bx:
        ans = True
        break

if ans:
    print('YES')
else:
    print('NO')