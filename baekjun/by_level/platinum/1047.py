import sys
from itertools import combinations


n = int(sys.stdin.readline())
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
tree = sorted(tree, key=lambda x:x[2], reverse=True)


def bndry(treecut):
    edge = [1000000, 1000000, 0, 0]
    pos_bndry = 0
    for i, t in enumerate(tree):
        if i in treecut:
            pos_bndry += t[2]
        else:
            edge[0] = min(edge[0], t[0])
            edge[1] = min(edge[1], t[1])
            edge[2] = max(edge[2], t[0])
            edge[3] = max(edge[3], t[1])

    lb = 2*(edge[2]-edge[0] + edge[3]-edge[1])
    return pos_bndry>=lb

num = 0
flag = True
while num<n+1 and flag:
    it = combinations(range(0, n), num)
    for case in it:
        if bndry(case):
            print(len(case))
            flag=False
            break
    num += 1