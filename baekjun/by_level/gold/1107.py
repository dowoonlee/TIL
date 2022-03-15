import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
ooo = list(map(int, sys.stdin.readline().split()))

def search(tnum, brk, op):
    brklist = [0]*11
    for i in brk:
        brklist[i] = 1

    cnum = tnum-1
    flag = True
    while flag:
        cnum += op
        cnumlist = list(map(int, str(cnum)))
        for i in cnumlist:
            if brklist[i]:
                flag=True
                break
            else:
                flag = False
    return abs(tnum-cnum) + len(cnumlist)

up = search(n, ooo, 1)
down = search(n, ooo, -1)
print(min([up, down, abs(n-100)]))

