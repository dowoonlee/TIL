import sys
#n = int(sys.stdin.readline())
#data = [sys.stdin.readline().strip() for i in range(n)]
n, data = 13, ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']

data = list(set(data))
wl = []
for i in range(len(data)):
    wl.append(len(data[i]))

ans = []
for i in sorted(list(set(wl))):
    dummy = []
    for j in range(len(wl)):
        if wl[j]==i:
            dummy.append(data[j])
    x = sorted(dummy)
    for k in range(len(dummy)):
        ans.append(x[k])
for i in ans:
    print(i)
