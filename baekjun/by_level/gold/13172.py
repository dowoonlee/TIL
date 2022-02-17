import sys
X = 1000000007

def fmodule(x, p, y):#(x^p)%y
    temp_p2 = bin(p)[2:]
    p2 = [int(temp_p2[i]) for i in range(len(temp_p2))][::-1]
    mody = [0]*len(p2)
    mody[0] = x%y
    for i, bt in enumerate(p2[1:]):
        mody[i+1] = (mody[i]**2)%y
    prod_mody = 1
    for i in range(len(mody)):
        if p2[i]:
            prod_mody *= mody[i]
    return prod_mody%y

def GCD(x, y):
   while y:
       x, y = y, x % y
   return x

m = int(sys.stdin.readline())
ans = 0
for _ in range(m):
    n, s = map(int, sys.stdin.readline().split())
    gcd = GCD(n, s)
    a, b = s//gcd, n//gcd
    ans += a * fmodule(b, X-2, X)

print(ans%X)

