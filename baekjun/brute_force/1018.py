import sys
n, m = map(int, sys.stdin.readline().split())

given_board = []

Bboard = []
Wboard = []

for i in range(8):
    BB, WW = [], []
    for j in range(8):
        BB.append((j+i)%2)
        WW.append((j+1+i)%2)
    Bboard.append(BB)
    Wboard.append(WW)

for i in range(n):
    data = sys.stdin.readline()
    binarys = []
    for j in data:
        if j=='B':
            binarys.append(0)
        elif j=='W':
            binarys.append(1)
        else:
            pass
    given_board.append(binarys)

subtB = []
subtW = []

for i in range(n-8+1):#garo if m=13, i:0~5
    for j in range(m-8+1):#sero
        disB, disW = 0, 0
        for p in range(8):#p:0~7
            garos = given_board[i+p][j:j+8]
            for q in range(8):
                disB+=abs(garos[q] - Bboard[p][q])
                disW+=abs(garos[q] - Wboard[p][q])
        subtB.append(disB)
        subtW.append(disW)

ans = [min(subtB), min(subtW)]
print(min(ans))





