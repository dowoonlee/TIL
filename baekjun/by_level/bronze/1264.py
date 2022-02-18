import sys

while True:
    ipt = str(sys.stdin.readline().rstrip())
    if ipt=="#":
        break
    else:
        ans=0
        for k in ipt:
            if k in "aeiouAEIOU":
                ans+=1
        print(ans)

