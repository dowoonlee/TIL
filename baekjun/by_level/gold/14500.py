import sys


n, m = map(int, sys.stdin.readline().split())

b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def t1(x, y):
    s = [0, 0, 0]
    try:
        s[0] = 0
        for i in range(4):
            s[0] += b[x][y + i]
    except IndexError:
        s[0] = -1
    try:
        s[1] = 0
        for i in range(4):
            s[1] += b[x + i][y]
    except IndexError:
        s[1] = -1
    try:
        s[2] = 0
        for i in range(2):
            for j in range(2):
                s[2] += b[x + i][y + j]
    except IndexError:
        s[2] = -1
    return max(s)


def t32(x, y):
    s = [0] * 8
    if x + 2 >= n or y + 1 >= m:
        return -1
    else:
        s[0] = b[x][y] + b[x][y + 1] + b[x + 1][y] + b[x + 2][y]
        s[1] = b[x][y + 1] + b[x + 1][y + 1] + b[x + 2][y + 1] + b[x + 2][y]
        s[2] = b[x][y] + b[x][y + 1] + b[x + 1][y + 1] + b[x + 2][y + 1]
        s[3] = b[x][y] + b[x + 1][y] + b[x + 2][y] + b[x + 2][y + 1]

        s[4] = b[x][y + 1] + b[x + 1][y + 1] + b[x + 1][y] + b[x + 2][y]
        s[5] = b[x][y] + b[x + 1][y] + b[x + 1][y + 1] + b[x + 2][y + 1]
        s[6] = b[x][y] + b[x + 1][y] + b[x + 1][y + 1] + b[x + 2][y]
        s[7] = b[x][y + 1] + b[x + 1][y + 1] + b[x + 1][y] + b[x + 2][y + 1]
    return max(s)


def t23(x, y):
    s = [0] * 8
    if x + 1 >= n or y + 2 >= m:
        return -1
    else:
        s[0] = b[x][y] + b[x + 1][y] + b[x + 1][y + 1] + b[x + 1][y + 2]
        s[1] = b[x][y] + b[x][y + 1] + b[x][y + 2] + b[x + 1][y + 2]
        s[2] = b[x][y] + b[x + 1][y] + b[x][y + 1] + b[x][y + 2]
        s[3] = b[x + 1][y] + b[x + 1][y + 1] + b[x + 1][y + 2] + b[x][y + 2]

        s[4] = b[x][y] + b[x][y + 1] + b[x + 1][y + 1] + b[x + 1][y + 2]
        s[5] = b[x + 1][y] + b[x + 1][y + 1] + b[x][y + 1] + b[x][y + 2]
        s[6] = b[x][y] + b[x][y + 1] + b[x + 1][y + 1] + b[x][y + 2]
        s[7] = b[x + 1][y] + b[x + 1][y + 1] + b[x][y + 1] + b[x + 1][y + 2]
    return max(s)


ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, t1(i, j))
        ans = max(ans, t23(i, j))
        ans = max(ans, t32(i, j))
print(ans)
