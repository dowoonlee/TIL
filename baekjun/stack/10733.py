import sys
k = int(sys.stdin.readline())
money = []
for i in range(k):
    n = int(sys.stdin.readline())
    if n:
        money.append(n)
    else:
        money.pop()
print(sum(money))