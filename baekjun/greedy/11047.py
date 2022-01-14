import sys

#n, k = map(int, sys.stdin.readline().split())
#coins = [int(sys.stdin.readline()) for _ in range(n)]
#n, k = 10, 4200
n, k = 10, 4790
coins = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
coins = coins[::-1]


rest = k
ans , i = 0, 0
while rest>0 and i <n:
    if rest<coins[i]:
        i+=1
        pass
    else:
        ans += rest//coins[i]
        rest = rest%coins[i]
        i+=1


print(ans)

