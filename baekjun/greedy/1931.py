import sys

#n = int(sys.stdin.readline())
#t = [[0, 0] for _ in range(n)]
#for i in range(n):
#    t[i][0], t[i][1] = map(int, sys.stdin.readline().split())

n = 11
t = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
t.sort(key=lambda x: (x[1], x[0]))
print(t)
i = 0
t_now = 0
nclass = 0
while i <n:
    c_now = t[i]
    if c_now[0]>=t_now:
        t_now = c_now[1]
        nclass+=1
    else:
        pass
    i+=1
print(nclass)