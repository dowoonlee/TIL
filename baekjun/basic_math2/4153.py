import sys
x = [1]
x = list(map(int, sys.stdin.readline().split()))

while x[0]:
    x = sorted(x)
    if x[0]**2+x[1]**2 == x[2]**2:
        print('right')
    else:
        print('wrong')
    x = list(map(int, sys.stdin.readline().split()))