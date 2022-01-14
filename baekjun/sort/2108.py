import sys
n = int(sys.stdin.readline())
data = []
count = [0]*(4000*2+1)

for i in range(n):
    x = int(sys.stdin.readline())
    data.append(x)
    count[x]+=1

print(round(sum(data)/len(data)))

print(sorted(data)[int(len(data)/2)])

mx = max(count)
mode = []
for i in range(-4000, 4001, 1):
    if count[i]==mx:
        mode.append(i)
if len(mode)==1:
    print(mode[0])
else:
    print(sorted(mode)[1])

print(max(data)-min(data))