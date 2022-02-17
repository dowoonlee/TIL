import sys
import time

r, c, t = map(int, sys.stdin.readline().split())
real_map = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
t0 = time.time()

circulator = []
for i in range(r):
    if real_map[i][0] == -1:
        circulator.append(i)

for _ in range(t):
    advec_map = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            cur_vel = real_map[i][j]
            if cur_vel>0:
                count = 0
                for d in range(4):
                    try:
                        if ((i + dx[d]==circulator[0]) or (i + dx[d]==circulator[1])) and (j + dy[d]==0):
                            pass
                        elif (i + dx[d]>=0) and (j + dy[d]>=0):
                            advec_map[i + dx[d]][j + dy[d]] += (cur_vel // 5)
                            count += 1
                    except IndexError:
                        pass
                advec_map[i][j] -= (cur_vel // 5) * count


    advec_map[circulator[0]][0], advec_map[circulator[1]][0] = 0, 0
    for i in range(r):
        for j in range(c):
            real_map[i][j] += advec_map[i][j]

    # upper part
    for i in range(circulator[0] - 1, 0, -1):  # left side
        real_map[i][0] = real_map[i - 1][0]
    for i in range(0, c - 1):  # upper side
        real_map[0][i] = real_map[0][i + 1]
    for i in range(0, circulator[0]):  # right side
        real_map[i][-1] = real_map[i + 1][-1]
    for i in range(c - 1, 0, -1):  # lower side
        real_map[circulator[0]][i] = real_map[circulator[0]][i - 1]
    real_map[circulator[0]][1]=0

    # lower part
    for i in range(circulator[1]+1, r - 1):  # left side
        real_map[i][0] = real_map[i + 1][0]
    for i in range(0, c - 1):  # lower side
        real_map[-1][i] = real_map[-1][i + 1]
    for i in range(r - 1, circulator[1], -1):  # right side
        real_map[i][-1] = real_map[i - 1][-1]
    for i in range(c - 1, 0, -1):  # upper side
        real_map[circulator[1]][i] = real_map[circulator[1]][i - 1]
    real_map[circulator[1]][1] = 0


totalsum = 0
for i in range(r):
    totalsum += sum(real_map[i])

print(totalsum+2)
print(time.time() - t0)
