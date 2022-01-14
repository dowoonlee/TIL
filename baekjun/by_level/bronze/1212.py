import sys

b8 = str(sys.stdin.readline().rstrip())

ans = bin(int(b8[0]))[2::]

if len(b8)==1:
    print(ans)

else:
    for n in b8[1::]:
        ans += '%03d'%(int(bin(int(n))[2::]))
    print(ans)

