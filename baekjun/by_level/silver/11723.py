import sys

n = int(sys.stdin.readline())

s = [0]*21

for _ in range(n):
    od = list(str(sys.stdin.readline().rstrip()).split())
    if od[0] == "add":
        s[int(od[1])] = 1
    elif od[0] == "remove":
        s[int(od[1])] = 0
    elif od[0] == "check":
        print(s[int(od[1])])
    elif od[0] == "toggle":
        s[int(od[1])] = 1 - s[int(od[1])]
    elif od[0] == "all":
        s = [1]*21
    else:
        s = [0]*21
