import sys


def conv(s):
    return [ord(s[0])-65, int(s[1])-1]

ps = [sys.stdin.readline().rstrip() for _ in range(36)]
ps.append(ps[0])

visited = [[0]*6 for _ in range(6)]

ans = "Valid"
for i in range(36):
    p = conv(ps[i])
    pn = conv(ps[i+1])
    if visited[p[0]][p[1]]:
        ans = "Invalid"
    else:
        visited[p[0]][p[1]] = 1
    dis = (p[0]-pn[0])**2 + (p[1]-pn[1])**2
    if dis!=5:
        ans = "Invalid"

print(ans)