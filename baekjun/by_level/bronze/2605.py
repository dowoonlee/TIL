import sys

n = int(sys.stdin.readline())
tickets = list(map(int, sys.stdin.readline().split()))
orders = [-1]*n
for i, ticket in enumerate(tickets):
    orders[i] = i - ticket
    for j in range(i):
        if orders[j]>=i-ticket:
            orders[j]+=1

ans = [0]*n
for i in range(n):
    ans[orders[i]] = str(i+1)
x = ' '.join(ans)
print(x)

