import sys
x, y = [0, 0, 0], [0, 0, 0]
nx, ny = [0, 0], [0, 0]

for i in range(3):
    x[i], y[i] = map(int, sys.stdin.readline().split())
ux, uy = list(set(x)), list(set(y))

for i in range(3):
    for j in range(2):
        if x[i]==ux[j]:
            nx[j]+=1
        if y[i]==uy[j]:
            ny[j]+=1
print(ux[nx.index(min(nx))], uy[ny.index(min(ny))])