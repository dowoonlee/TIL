import sys

octo = {
    '-': 0,
    '\\':1,
    '(' :2,
    '@':3,
    '?':4,
    '>':5,
    '&':6,
    '%':7,
    '/':-1
}
ipt = sys.stdin.readline().rstrip()

while ipt!="#":
    ans = 0
    for i in range(len(ipt)):
        ans += octo[ipt[-1-i]]*(8**i)
    print(ans)
    ipt = sys.stdin.readline().rstrip()