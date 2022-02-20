import sys

n = int(sys.stdin.readline())

while n>=4:
    x = sorted(list(set(str(n))))
    if x==['4', '7'] or x==['4'] or x==['7']:
        print(n)
        break
    else:
        n-=1
