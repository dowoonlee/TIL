import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for i in range(n)]
data = sorted(data)

dif = [data[i+1]-data[i] for i in range(n-1)]

dif = sorted(dif)[::-1]

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

mx = dif[0]
for i in range(n-2):
    mx = GCD(mx, dif[i+1])

ans = []
for i in range(2, int(mx**0.5)+1, 1):
    if mx%i==0:
        ans.append(i)
        ans.append(int(mx/i))

ans.append(mx)
ans = list(set(ans))
ans = sorted(ans)
for i in ans:
    print(i)