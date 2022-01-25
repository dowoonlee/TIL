import sys

x = str(sys.stdin.readline().rstrip())

ans = x[0] + x[1] + x[2::][::-1]


for i in range(1, len(x)-1, 1):
    for j in range(i+1, len(x),1):
        nx = x[0:i][::-1] + x[i:j][::-1] + x[j::][::-1]
        ans = sorted([ans, nx])[0]

print(ans)

