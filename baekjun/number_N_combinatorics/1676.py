import sys

n = int(sys.stdin.readline())
ft = [0, 0]
for i in range(3):
    ft[0] += n//(5**(i+1))
for i in range(9):
    ft[1] += n//(2**(i+1))

print(min(ft))
