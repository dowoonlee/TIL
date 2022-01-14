import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    sc = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    sc.sort(key=lambda x: (x[0], x[-1]))
    j, min2 = 1, sc[0][1]
    ans = 1
    while j < n:
        if sc[j][1] < min2:
            ans += 1
            min2 = sc[j][1]
        else:
            pass
        j+=1
    print(ans)





