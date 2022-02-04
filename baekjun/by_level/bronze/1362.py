import sys

ipt_ar = True
cond = True
i = 0
ans = []

while cond:
    if ipt_ar:
        o, w = map(int, sys.stdin.readline().split())
        death = False
        ipt_ar = False
        i+=1
        if o == 0 and w == 0:
            cond=False
            break
    else:
        emot, n = map(str, sys.stdin.readline().split())
        if emot=='#':
            if w>o/2 and w<2*o and not death:
                ans.append(":-)")
            elif w<=0 or death:
                ans.append("RIP")
            else:
                ans.append(":-(")
            ipt_ar = True
        else:
            n = int(n)
            if emot == 'F':
                w += n
            elif emot == 'E':
                w -= n
            if w<=0:
                death = True

for i ,v in enumerate(ans):
    print(i+1, v)