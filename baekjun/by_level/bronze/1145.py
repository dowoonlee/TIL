import sys

x = list(map(int, sys.stdin.readline().split()))
x.sort()
cv = x[0]

n = 0
while n < 3:
    n = 0
    for i in range(5):
        if cv%x[i]==0:
            print(cv, x[i])
            n+=1
    cv+=1

print(cv-1)

