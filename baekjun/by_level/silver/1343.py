import sys

t = str(sys.stdin.readline().rstrip())
a = [0]*len(t)
for i in range(len(t)):
    if t[i] == 'X':
        a[i] = 1

st = 0
bp = False
ans=""
for i in range(len(t)):
    if a[i] == 0:
        if st%2 == 0:
            aaaa = (st//4)
            bb = (st%4)//2
            ans += ("AAAA"*aaaa + "BB" * bb)
        else:
            bp = True
        ans+='.'
        st = 0

    else:
        st += 1

    if bp:
        ans = -1
        break


if st%2 == 0 and not bp:
    aaaa = (st//4)
    bb = (st%4)//2
    ans += ("AAAA"*aaaa + "BB" * bb)
else:
    ans = -1


print(ans)