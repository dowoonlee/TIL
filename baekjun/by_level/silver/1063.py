import sys

move = {'R': [1, 0],
        'L': [-1, 0],
        'B': [0, -1],
        'T': [0, 1],
        'RT': [1, 1],
        'LT': [-1, 1],
        'RB': [1, -1],
        'LB': [-1, -1]}

king_ipt, stone_ipt, N_ipt = map(str, sys.stdin.readline().split())
N = int(N_ipt)
king = [ord(king_ipt[0])-64, int(king_ipt[1])]#1~8
stone = [ord(stone_ipt[0])-64, int(stone_ipt[1])]

for _ in range(N):
    mv = move[str(sys.stdin.readline().rstrip())]
    ok = True

    temp_king = [mv[i]+king[i] for i in range(2)]
    temp_stone = stone
    if temp_king[0]<1 or temp_king[0]>8 or temp_king[1]<1 or temp_king[1]>8:#out of board
        ok = False
    if temp_king[0]==stone[0] and temp_king[1]==stone[1]:
        temp_stone = [mv[i]+stone[i] for i in range(2)]
        if temp_stone[0]<1 or temp_stone[0]>8 or temp_stone[1]<1 or temp_stone[1]>8:
            ok = False
    if ok:
        king = temp_king
        stone= temp_stone
    else:
        pass

print(chr(king[0]+64)+str(king[1]))
print(chr(stone[0]+64)+str(stone[1]))

