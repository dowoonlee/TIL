import sys

a = [int(i) for i in sys.stdin.readline().rstrip()]
p = [int(i) for i in sys.stdin.readline().rstrip()]
k = len(p)


l = k+1
while True:
    b = [0] * l
