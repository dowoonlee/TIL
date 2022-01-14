import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

def kse(x, k):
    for i in range(2, k+1):
        while x%i==0:
            x/=i
    if x==1:
        return True
    else:
        return False

ans=0
for i in range(n, 1, -1):
    if kse(i, k):
        ans+=1
print(ans+1)
