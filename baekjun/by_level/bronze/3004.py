import sys

n = int(sys.stdin.readline())

#1 2 3 4 5 6 7 8 9
#0 0 1 1 2 2 3 3
#2 4 6 9 12 16



ans = 1
for i in range(1, n+1):
    ans += ((i+2)//2)
print(ans)