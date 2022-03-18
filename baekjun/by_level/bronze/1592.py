import sys
n, m, l = map(int ,sys.stdin.readline().split())

fr = [0]*n
idx = 0
fr[0]=1

if m==1:
    print(0)
else:
    flag = True
    while flag:
        idx = (idx+(-1)**(fr[idx]%2+1)*l + 2 * n) % n
        fr[idx]+=1
        if fr[idx]==m:
            flag=False


    print(sum(fr)-1)

