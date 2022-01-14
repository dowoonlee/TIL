import sys

x = int(sys.stdin.readline())
while x:
    y = int(str(x)[::-1])
    if x==y:
        print('yes')
    else:
        print('no')
    x = int(sys.stdin.readline())

