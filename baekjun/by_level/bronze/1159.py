import sys
n = int(sys.stdin.readline())
name = [str(sys.stdin.readline().rstrip()) for _ in range(n)]
l1 = [i[0] for i in name]
l2 = list(set(l1))
n1 = [0]*len(l2)
for k in l1:
    for j in range(len(l2)):
        if k==l2[j]:
            n1[j]+=1
ans = []
for i in range(len(l2)):
    if n1[i]>=5:
        ans.append(l2[i])

if ans:
    ans.sort()
    print("".join(ans))
else:
    print('PREDAJA')
