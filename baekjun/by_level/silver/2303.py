import sys
from itertools import combinations

n = int(sys.stdin.readline())
cards = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ft = list(combinations([0,1,2,3,4], 2))

def endof(card):
    sc0 = sum(card)
    maxv = 0
    for comb in ft:
        sc = sc0
        for c in comb:
            sc -= card[c]
        maxv = max(maxv, sc%10)
    return maxv

ans_arr = [endof(cards[i]) for i in range(n)]
maxv = max(ans_arr)
for i in range(n-1, -1, -1):
    if ans_arr[i]==maxv:
        print(i+1)
        break
