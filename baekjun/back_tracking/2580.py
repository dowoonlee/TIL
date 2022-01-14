import sys

#data = []
#for i in range(9):
#    data.append(list(map(int,sys.stdin.readline().split())))

data = [[0, 3, 5, 4, 6, 9, 2, 7, 8], [7, 8, 2, 1, 0, 5, 6, 0, 9], [0, 6, 0, 2, 7, 8, 1, 3, 5], [3, 2, 1, 0, 4, 6, 8, 9, 7], [8, 0, 4, 9, 1, 3, 5, 0, 6], [5, 9, 6, 8, 2, 0, 4, 1, 3], [9, 1, 7, 6, 5, 2, 0, 8, 0], [6, 0, 3, 7, 0, 1, 9, 5, 2], [2, 5, 8, 3, 9, 4, 7, 6, 0]]
zeros = [(i, j) for i in range(9) for j in range(9) if data[i][j] == 0]

def w3check(x, y):
    row = data[x]
    col = [data[i][y] for i in range(9)]
    box = []
    for i in [3*(x//3)+i for i in range(3)]:
        for j in [3*(y//3)+i for i in range(3)]:
            box.append(data[i][j])

    dset = []
    for i in range(9):
        dset.append(row[i])
        dset.append(col[i])
        dset.append(box[i])
    dset = sorted(list(set(dset)))[1::]

    base = [i+1 for i in range(9)]
    for i in dset:
        base.remove(i)
    return base

flag=False
def dfs(x):
    global flag

    if flag:  # 이미 답이 출력된 경우
        return

    if x == len(zeros):  # 마지막 0까지 다 채웠을 경우
        for row in data:
            print(*row)
        flag = True  # 답 출력
        return

    else:
        (i, j) = zeros[x]
        promising = w3check(i, j)  # 유망한 숫자들을 받음

        for num in promising:
            data[i][j] = num  # 유망한 숫자 중 하나를 넣어줌
            dfs(x + 1)  # 다음 0으로 넘어감
            data[i][j] = 0  # 초기화 (정답이 없을 경우를 대비)

dfs(0)
