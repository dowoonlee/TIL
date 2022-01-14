import sys
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)
t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    if m < 2 * n:
        n = m - n

    denominator = [i + 1 for i in range(n)]  # 분모
    numerater = [m - i for i in range(n)]  # 분자

    for i in range(n):
        for j in range(n):
            if numerater[i] == 1:
                pass
            else:
                if denominator[j] > numerater[i]:
                    gcd = GCD(denominator[j], numerater[i])
                else:
                    gcd = GCD(numerater[i], denominator[j])
                denominator[j] /= gcd
                numerater[i] /= gcd
    ans = 1
    for i in numerater:
        ans*=i
    print(int(ans))