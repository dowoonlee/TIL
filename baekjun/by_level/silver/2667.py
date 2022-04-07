import sys

n = int(sys.stdin.readline())
apart = [[0]*n for _ in range(n)]
for i in range(n):
    ipt = sys.stdin.readline().rstrip()
    for j in range(n):
        apart[i][j] = int(ipt[j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def search(root):
    q = []
    q.append(root)

    ngroup = 1
    while q:
        adr = q.pop()
        for d in range(4):
            nx = adr[0] + dx[d]
            ny = adr[1] + dy[d]

            if (nx>=0 and nx<n and ny>=0 and ny<n) and (apart[nx][ny] == 1):
                apart[nx][ny] = -1
                q.append([nx, ny])
                ngroup += 1
    if ngroup!=1:
        ngroup-=1
    return ngroup


apt = []
for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            ngroup = search([i, j])
            apt.append(ngroup)
apt.sort()

print(len(apt))
for i in range(len(apt)):
    print(apt[i])

