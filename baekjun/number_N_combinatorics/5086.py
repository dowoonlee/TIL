import sys
a, b = map(int, sys.stdin.readline().split())

while a:
    if b%a==0:
        print('factor')
    elif a%b==0:
        print('multiple')
    else:
        print('neither')
    a, b = map(int, sys.stdin.readline().split())