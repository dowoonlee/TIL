import sys
n0 = int(sys.stdin.readline())
n = n0
a = -1

cycle = 0
while a!=n0:
    a = (n%10)*10 + (n//10 + n%10)%10
    n = a
    cycle+=1
print(cycle)

