import sys

n = int(sys.stdin.readline())

data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

B, W = 0, 0

def bw(paper):
    global B
    global W
    size = len(paper)
    if sum(map(sum, paper))==size**2:
        B+=1
    elif sum(map(sum, paper))==0:

        W+=1
    else:
        p1 = [paper[0:int(size / 2)][i][0:int(size / 2)] for i in [i for i in range(int(size / 2))]]
        p2 = [paper[0:int(size / 2)][i][int(size / 2)::] for i in [i for i in range(int(size / 2))]]
        p3 = [paper[int(size / 2)::][i][0:int(size / 2)] for i in [i for i in range(int(size / 2))]]
        p4 = [paper[int(size / 2)::][i][int(size / 2)::] for i in [i for i in range(int(size / 2))]]
        bw(p1)
        bw(p2)
        bw(p3)
        bw(p4)
bw(data)
print(W)
print(B)


