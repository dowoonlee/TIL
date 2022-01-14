import sys
h, m = map(int, sys.stdin.readline().split())


time = 60 * h + m - 45
if time<0:
    time+=60*24

hr = time//60
mn = time%60

print(hr, mn)

