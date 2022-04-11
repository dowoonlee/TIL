import sys

t = int(sys.stdin.readline())


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

    g = gcd(m, n)

    if x % g != y % g:
        print(-1)

    else:
        l = lcm(m, n)
        p, q = ex_euclid(m, n)
        print(p, q)


        test = (m//g)*p + (n//g)*q

        ans = (x * (n // g) * q + y * (m // g) * q) % l
        print(ans)
