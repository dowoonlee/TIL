import sys

ult = 1000000007



n, k = map(int, sys.stdin.readline().split())


def factorial_modular(n, md):
    res = 1
    for i in range(n):
        res = (res * (i+1))%md
    return res

def expo_modular(x, ult):
    bin_ult = bin(ult-2)[2::]#exponential p-2 part, format as binary
    modb = [0] * len(bin_ult)
    modb[0] = x % ult

    for i in range(len(bin_ult) - 1):
        modb[i + 1] = (modb[i] * modb[i]) % ult
    res = 1

    for i in range(len(modb)):
        if int(bin_ult[::-1][i]):
            res *= modb[i]

    return res % ult



a = factorial_modular(n, ult)# n!%p
b = factorial_modular(n-k, ult)# ((n-k)!)^(p-2)%p part except ^(p-2)
c = factorial_modular(k, ult)#(k!)^(p-2)%p part except ^(p-2)

ans = (a * (expo_modular(b, ult)) * (expo_modular(c, ult)))%ult
print(ans)

