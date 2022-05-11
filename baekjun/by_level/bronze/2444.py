import sys

n = int(sys.stdin.readline())


for i in range(n-1):
    nb = n-1-i
    ns = 2*i+1
    print(" "*nb+"*"*ns)
print("*"*(2*n-1))
for i in range(n-1):
    nb = i+1
    ns = 2*(n-i-1)-1
    print(" "*nb+"*"*ns)