import sys

n = int(sys.stdin.readline())

sq = []
i = 1
while i**2<n:
    sq.append(i**2)
    i+=1
print(sq)