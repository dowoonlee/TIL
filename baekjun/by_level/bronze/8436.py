import sys

ipt = sys.stdin.readline().rstrip()

ans = 1
for w in ipt:
    if w=="T":
        ans*=2
    elif w=="D":
        ans*=2
    elif w=="L":
        ans*=2
    elif w=="F":
        ans*=2
print(ans)