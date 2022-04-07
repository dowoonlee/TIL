import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = str(sys.stdin.readline().rstrip())


def kmp(given, p):
    ls = len(given)
    lp = len(p)

    pi = [0] * lp
    for i in range(2, lp):
        pi[i] = i - 1

    idx = 0
    cnt = 0
    i = 0
    while i < ls:
        while idx > 0 and given[i] != p[idx]:
            idx = pi[idx - 1]
        if given[i] == p[idx]:
            if idx == lp - 1:
                cnt += 1
                i -= (2 * (n-1))
                idx = 0
            else:
                idx += 1
                i += 1
        else:
            i += 1
    return cnt


ans = kmp(s, "IO" * n + "I")
print(ans)
