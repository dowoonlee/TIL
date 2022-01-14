import sys

b = "0b"+str(sys.stdin.readline())
d = int(b, 2)
o = oct(d)

print(o[2::])