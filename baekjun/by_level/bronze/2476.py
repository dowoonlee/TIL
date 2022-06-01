import sys

n = int(sys.stdin.readline())

mv = 0
for _ in range(n):
    dice = list(map(int, sys.stdin.readline().split()))
    ndice = [0]*6
    for i in range(3):
        ndice[dice[i]-1] += 1
    cnt = max(ndice)
    if cnt==3:
        price = dice[0]*1_000+10_000
    elif cnt ==2:
        for i in range(6):
            if ndice[i]==2:
                price = (i+1)*100+1_000
                break
    else:
        price = max(dice)*100
    mv = max(mv, price)
print(mv)

