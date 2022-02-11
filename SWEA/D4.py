import sys
import matplotlib.pyplot as plt

tc = int(sys.stdin.readline())

ladder=[]
for _ in range(100):
    ladder.append(list(map(int, sys.stdin.readline().split())))
for i in range(100):
    if ladder[99][i]==2:
        p = i
        break

for lev in range(98, -1, -1):
    ladder[lev+1][p]=2

    if ladder[lev][p-1]==1:
        nextp = p-1
        while nextp==1:
            nextp-=1
        print("-", lev, ladder[lev][p - 2:p + 3], abs(p-nextp+1))
        p = nextp+1
    elif ladder[lev][p+1]==1:
        nextp=p+1
        while nextp==1:
            nextp+=1
        print("+", lev, ladder[lev][p - 2:p + 3], abs(p - nextp + 1))
        p = nextp-1
    else:
        print(lev, 'straight')
        pass
print(p)
plt.imshow(ladder)
plt.show()
