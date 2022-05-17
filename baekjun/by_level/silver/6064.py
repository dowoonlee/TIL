import sys

t = int(sys.stdin.readline())

print()
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def ex_euclid(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b:
        n, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - n * x1
        y0, y1 = y1, y0 - n * y1
    return x0, y0


for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    d = x - y

    g = gcd(m, n)
    a, b = ex_euclid(m, n)

    if d%g:
        ans = -1

    else:
        k = d // g
        kk = x- k*a*m
        print(kk)
        ans = (kk-1) % (m//g*n) + 1
        print(kk-1, m//g*n, (kk-1)%(m//g*n))
    #print(ans)
