import sys

n = int(sys.stdin.readline())

for i in range(n-1):
    ns = i+1
    nb = 2*n-ns*2
    print("*"*ns + " "*nb+"*"*ns)
print("*"*(2*n))
for i in range(n-1):
    ns = n-i-1
    nb = 2*n-ns*2
    print("*"*ns + " "*nb+"*"*ns)