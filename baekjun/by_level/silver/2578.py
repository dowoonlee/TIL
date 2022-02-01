import sys

board = []
for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().split())))

breakcond = False
for i in range(5):
    ipt = list(map(int, sys.stdin.readline().split()))
    for j in range(5):


        for bx in range(5):
            for by in range(5):
                if board[bx][by]==ipt[j]:
                    board[bx][by] = 0
                    break

        cnt = 0
        for x in range(5):
            if sum(board[x]) == 0:
                cnt += 1
        for y in range(5):
            temp = 0
            for t in range(5):
                temp += board[t][y]
            if temp==0:
                cnt += 1
        diag1, diag2 = 0, 0
        for k in range(5):
            diag1 += board[k][k]
            diag2 += board[k][4-k]
        if diag1==0:
            cnt+=1
        if diag2==0:
            cnt+=1

        if cnt>=3:
            ans = 5*i+j+1
            breakcond = True
            break
    if breakcond:
        break
print(ans)








