import sys

n = 1
scene = 1
while n:

    n = int(sys.stdin.readline())
    name = [sys.stdin.readline().rstrip() for _ in range(n)]
    isear = [0]*n

    for _ in range(2*n-1):
        ipt = list(map(str, sys.stdin.readline().split()))
        isear[int(ipt[0])-1]+=1

    for i in range(n):
        if isear[i]<2:
            print(scene, name[i])
            scene += 1
            break
