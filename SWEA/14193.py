t = int(input())


def search(root):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = []
    q.append(root)
    cnt = 0

    while q:
        node = q.pop()
        for d in range(4):
            nx = node[0] + dx[d]
            ny = node[1] + dy[d]

            if (nx >= 0 and nx < y and ny >= 0 and ny < x) and not visited[nx][ny] and field[nx][ny]>=0:
                if field[nx][ny]>=1:
                    return cnt

                else:
                    cnt+=1
                    q.append([nx, ny])
                    visited[nx][ny] = 1


for tc in range(1, t + 1):
    x, y = map(int, input().split())

    field = [[0] * x for _ in range(y)]
    cnt = 0
    for i in range(y):
        ipt = input().rstrip()
        for j in range(x):
            if ipt[j] == "#":
                field[i][j] = -1
            elif ipt[j] == "S" or ipt[j] == "A":
                cnt += 1
                field[i][j] = cnt

            else:
                field[i][j] = 0

    visited = [[0] * x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            if field[i][j]>=1 and not visited[i][j]:
                w = search([i, j])
                print(w)
    print(cnt - 1)
