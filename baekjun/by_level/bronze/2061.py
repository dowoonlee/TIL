import sys
k, l = map(int, sys.stdin.readline().split())

cond = True
for pn in range(2, l):
    if k%pn:
        pass
    else:
        print("BAD", pn)
        cond = False
        break
if cond:
    print("GOOD")
