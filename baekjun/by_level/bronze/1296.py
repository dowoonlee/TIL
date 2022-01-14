import sys

name = str(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())

def cal(t):
    love = [0] * 4
    for i in t:
        if i=='L':
            love[0]+=1
        elif i=='O':
            love[1]+=1
        elif i=='V':
            love[2]+=1
        elif i=='E':
            love[3]+=1
        else:
            pass
    return love

ylove = cal(name)

winrate = [0]*n
teams = []
for i in range(n):
    team = str(sys.stdin.readline().rstrip())
    teams.append(team)
    tlove = cal(team)
    l, o, v, e = (tlove[0]+ylove[0]), (tlove[1]+ylove[1]), (tlove[2]+ylove[2]), (tlove[3]+ylove[3])
    winrate[i] = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100

maxv = max(winrate)
cand = []
for i in range(n):
    if winrate[i]==maxv:
        cand.append(teams[i])
cand.sort()
print(cand[0])
