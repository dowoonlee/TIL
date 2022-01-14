import sys
#n = int(sys.stdin.readline())
#data = []
#for i in range(n):
#    data.append(list(map(int,sys.stdin.readline().split())))
n=5
data = [[0, 4], [1, 2], [1, -1], [2, 2], [3, 3]]
print(data)

data.sort(key=lambda x: (x[-1], x[0]))
for i in range(n):
    print('%d %d'%(data[i][0], data[i][1]))