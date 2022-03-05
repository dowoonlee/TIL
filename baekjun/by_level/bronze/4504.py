import sys

n = int(sys.stdin.readline())
x = int(sys.stdin.readline())
while x:
    if x%n:
        print("%d is NOT a multiple of %d."%(x, n))
    else:
        print("%d is a multiple of %d." % (x, n))
    x = int(sys.stdin.readline())