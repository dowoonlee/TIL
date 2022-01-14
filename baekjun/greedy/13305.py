import sys

#n = int(sys.stdin.readline())
#l = list(map(int, sys.stdin.readline().split()))
#cost = list(map(int, sys.stdin.readline().split()))
#cost = cost[0:-1]


n = 4
nroad = [2, 3, 1]
cost = [5, 2, 4]
road=[nroad[0]]
for i in range(1, n-1):
    road.append(road[i-1]+nroad[i])
print(road)

cur_road = 0
cur_cost = 0
min_cost = cost[0]
ans=0

for pos in range(1, road[-1]):
    print('POS =', pos)
    if pos>road[cur_road]:
        cur_road += 1
        cur_cost += 1
        min_cost = min(min_cost, cost[cur_cost])
    ans += min_cost
    print('COST:', min_cost, 'ANS:', ans)
    print('-------------')



print('ANS =', ans+min_cost)







