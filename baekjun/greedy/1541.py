import sys

eq = sys.stdin.readline()
n, op = [], []

st, ed = 0, 0
for s in eq:
    if s=='+'or s== '-':
        n.append(int(eq[st:ed]))
        op.append(eq[ed])
        ed+=1
        st=ed
    else:
        ed+=1
n.append(int(eq[st:ed]))


i=1
n_fin = [n[0]]
while i<len(n):
    if op[i-1]=='+':
        n_fin[-1]+=n[i]
        i+=1
    else:
        n_fin.append(n[i])
        i+=1
print(n_fin)

ans = n_fin[0]
for i in range(1, len(n_fin)):
    ans-=n_fin[i]
print(ans)

