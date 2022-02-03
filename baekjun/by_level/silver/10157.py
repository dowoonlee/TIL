import sys
c, r = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
room = [[0]*(r+1) for _ in range(c+1)]

for i in range(r+1):
    room[0][i] = 0.1
for i in range(c+1):
    room[i][0] = 0.1

if k>c*r:
    print(0)
else:
    x = [1, 1]
    direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(k-1):
        room[x[0]][x[1]] = i+1

        try:
            next_block = room[x[0]+direc[0][0]][x[1]+direc[0][1]]
            if next_block>0:
                direc = direc[1:] + direc[0:1]
            x[0] += direc[0][0]
            x[1] += direc[0][1]
        except IndexError:
            direc = direc[1:] + direc[0:1]

            x[0] += direc[0][0]
            x[1] += direc[0][1]

    print(x[0], x[1])




