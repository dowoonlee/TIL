import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())


ans = abs(100-n)
if m:
    ooo = set(sys.stdin.readline().split())
else:
    ooo = set()

for num in range(1000001):
    for x in str(num):
        if x in ooo:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num-n))

print(ans)



