import sys

#n = int(sys.stdin.readline())

#ans = []

#next) i=k or i=k+1
#for _ in range(n):
#    ans.append(list(map(int, sys.stdin.readline().split())))
#print(ans)

n ,ans =5, [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
for i in range(n-1, 0, -1):
    for j in range(i):
        ans[i-1][j] += max(ans[i][j], ans[i][j+1])


print(ans[0][0])
