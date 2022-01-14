import sys

n, new_score, p = map(int, sys.stdin.readline().split())
if n == 0:
    print(1)
else:
    ranking = list(map(int, input().split()))
    if n == p and ranking[-1] >= new_score:
        print(-1)
    else:
        rank = n + 1
        for i in range(n):
            if ranking[i] <= new_score:
                rank = i + 1
                break
        print(rank)