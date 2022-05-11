import sys

wa = sys.stdin.readline().rstrip()
wb = sys.stdin.readline().rstrip()

ra = [0]*30
rb = [0]*30
a = ord("a")

for i in range(len(wa)):
    ra[ord(wa[i])-a] += 1
for i in range(len(wb)):
    rb[ord(wb[i])-a] += 1

s = 0
for i in range(30):
    s += abs(ra[i]-rb[i])
print(s)

