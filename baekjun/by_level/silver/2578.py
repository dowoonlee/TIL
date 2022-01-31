import sys

bingo = []
for _ in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))

bx, by, bd = [0]*5, [0]*5, [0]*2
finalcond = False
for i in range(5):
    given = list(map(int,sys.stdin.readline().split()))
    for j, number in enumerate(given):
        curb=0
        breakcond = False
        for x in range(5):
            for y in range(5):
                if bingo[x][y]==number:
                    bx[x]+=1
                    by[y]+=1
                    if x==y:
                        bd[0]+=1
                    if x+y==4:
                        bd[1]+=1
                    breakcond = True
            if breakcond:
                break
        for k in range(5):
            if bx[k]==5:
                curb+=1
            if by[k]==5:
                curb+=1
        for k in range(2):
            if bd[k]==5:
                curb+=1
        if curb==3:
            ans = 5*i+j+1
            finalcond=True
            break
    if finalcond:
        break
print(ans)







