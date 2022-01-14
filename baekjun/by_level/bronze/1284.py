import sys

x = int(sys.stdin.readline())
while x:
    ans = len(str(x))+1
    for n in str(x):
        if int(n)==1:
            ans+=2
        elif int(n)==0:
            ans+=4
        else:
            ans+=3
    print(ans)
    x = int(sys.stdin.readline())

