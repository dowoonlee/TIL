import sys

k = int(sys.stdin.readline())
x, y = [0], [0]
for _ in range(6):
    direc, dx = map(int, sys.stdin.readline().split())
    if direc == 1:
        x.append(x[-1] + dx)
        y.append(y[-1])
    elif direc == 2:
        x.append(x[-1] - dx)
        y.append(y[-1])
    elif direc == 3:
        x.append(x[-1])
        y.append(y[-1] + dx)
    else:
        x.append(x[-1])
        y.append(y[-1] - dx)
x = x[0:6]
y = y[0:6]

uniq_x, uniq_y = sorted(list(set(x))), sorted(list(set(y)))
for i in range(6):
    if x[i]==uniq_x[1] and y[i]==uniq_y[1]:
        idx = i
        break
x = x[idx:]+(x[0:idx])
y = y[idx:]+(y[0:idx])
s = 0
for i in range(1, 5):
    s += ((x[i]*y[0] + x[i+1]*y[i] + x[0]*y[i+1]) - (x[0]*y[i] + x[i]*y[i+1] + x[i+1]*y[0]))/2

print(int(k*s))


