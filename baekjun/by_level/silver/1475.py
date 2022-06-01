import sys

num = sys.stdin.readline().rstrip()

cnt = [0] * 9
for n in num:
    nn = int(n)
    if nn == 9:
        cnt[6] += 1
    else:
        cnt[nn] += 1

cnt[6] = cnt[6] // 2 + cnt[6] % 2

print(max(cnt))
