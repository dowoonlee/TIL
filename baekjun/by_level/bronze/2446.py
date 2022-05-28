import sys
n = int(sys.stdin.readline())

for i in range(n-1):
    nb = i
    ns = 2*n-1-2*nb
    print(" "*nb+"*"*ns)
print(" "*(n-1)+"*")
for i in range(n-1):
    nb = n-2-i
    ns = 2*(i+1)+1
    print(" "*nb+"*"*ns)