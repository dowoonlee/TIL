import sys

data = [int(sys.stdin.readline()) for i in range(10)]
R = [i%42 for i in data]
uniqR = set(R)

print(len(uniqR))



