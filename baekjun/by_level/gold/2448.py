import sys

n = int(sys.stdin.readline())
k = 0
while (n//3)/2**k>1:
    k+=1
#n=24 => k=3
graph = [[" "] * 2 * n for _ in range(n)]


def pascal(x, y, depth):
    if depth==0:
        graph[x][y] = "*"# head of tri
        graph[x+1][y+1], graph[x+1][y-1] = "*", "*"
        for i in range(-2, 3):
            graph[x+2][y+i] = "*"
    else:
        pascal(x, y, depth-1)
        pascal(x + 3*2**(depth-1), y - 3*2**(depth-1), depth-1)
        pascal(x + 3*2**(depth-1), y + 3*2**(depth-1), depth-1)

pascal(0, n-1, k)
for i in graph:
    print("".join(i))



