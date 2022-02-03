import sys

w, h = map(int, sys.stdin.readline().split())
wlist, hlist = [1]*w, [1]*h
n = int(sys.stdin.readline())
for _ in range(n):
    vh, x = map(int, sys.stdin.readline().split())
    if vh:#vertical
        i, s = 0, 0
        while s < x:
            s += wlist[i]
            i += 1
        wlist = wlist[0:i] + [0] + wlist[i:]
    else:
        i, s = 0, 0
        while s < x:
            s += hlist[i]
            i += 1
        hlist = hlist[0:i] + [0] + hlist[i:]

mh, mw = [0], [0]
for hs in hlist:
    if hs==1:
        mh[-1]+=1
    else:
        mh.append(0)
for ws in wlist:
    if ws==1:
        mw[-1]+=1
    else:
        mw.append(0)
print(max(mh)* max(mw))







