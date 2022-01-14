import sys
n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

r1 = data[0]
rings = data[1::]

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

ans0, ans1 = [], []

for ring in rings:
    if r1>ring:
        gcd = GCD(r1, ring)
        ans0.append(r1/gcd)
        ans1.append(ring/gcd)
    elif r1<ring:
        gcd = GCD(ring, r1)
        ans0.append(r1/gcd)
        ans1.append(ring/gcd)
    else:
        ans0.append(1)
        ans1.append(1)

for i in range(n-1):
    print('%d/%d'%(ans0[i], ans1[i]))

