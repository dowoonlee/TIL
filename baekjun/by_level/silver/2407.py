import sys

n, m = map(int, sys.stdin.readline().split())

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

if n-m<m:
    m = n-m


head = [n-i for i in range(m)]
tail = [i+1 for i in range(m)]

for i in range(m):
    for j in range(m):
        gcd = GCD(head[i], tail[j])
        head[i] //= gcd
        tail[j] //= gcd
ans = 1
for i in range(m):
    ans *= head[i]
print(ans)
