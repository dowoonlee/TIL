import sys

n = int(sys.stdin.readline())
ans = 0
while n>0:
    k=0
    sumk=0
    while sumk<=n:
        k += 1
        sumk+=k
    sumk-=k
    n -= sumk
    ans+=(k-1)
print(ans)

