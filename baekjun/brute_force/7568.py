import sys
"""
n = int(sys.stdin.readline())
x = []
y = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)
"""
n =5
x = [55, 58, 88, 60, 46]
y = [185, 183, 186, 175, 155]

rank = [1]*n

for i in range(n):
    p, q = x[i], y[i]
    for j in range(n):
        if i==j:
            pass
        else:
            dw, dh = x[j]-p, y[j]-q
            if dw>0 and dh>0:
                rank[i]+=1

ans=''
for i in range(n-1):
    ans+='%d '%rank[i]
ans+='%d'%rank[-1]
print(ans)