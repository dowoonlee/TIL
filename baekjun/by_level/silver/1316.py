import sys

n = int(sys.stdin.readline())

ans = 0
for _ in range(n):
    group = True
    w = str(sys.stdin.readline().rstrip())
    enlist = ''

    for k in w:
        if k in enlist and k==enlist[-1]:
            pass
        elif k in enlist and k!=enlist[-1]:
            group = False
            break
        else:
            enlist += k
    if group:
        ans+=1
print(ans)



