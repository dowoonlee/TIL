import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
dpinc = [1] * n
dpdec = [1] * n

for i in range(1, n):
    if seq[i] <= seq[i-1]:
        dpdec[i] = max(dpdec[i], dpdec[i-1]+1)
    if seq[i] >= seq[i-1]:
        dpinc[i] = max(dpinc[i], dpinc[i-1]+1)
print(max(max(dpinc), max(dpdec)))