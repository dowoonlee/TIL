import sys

###한 개의 정수를 입력받을 때
#n = int(sys.stdin.readline())

###정해진 개수의 정수를 한줄에 입력받을 때
#a, b = map(int, sys.stdin.readline().split())

###임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
#data = list(map(int,sys.stdin.readline().split()))


###임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
#data = []
#n = int(sys.stdin.readline())
#for i in range(n):
#    data.append(list(map(int,sys.stdin.readline().split())))

###문자열 n줄을 입력받아 리스트에 저장할 때
#import sys
#n = int(sys.stdin.readline())
#data = [sys.stdin.readline().strip() for i in range(n)]

from collections import deque


def solution(n, edges):
    maxV = 0
    for edge in edges:
        maxV = max([edge[0], edge[1], maxV])

    graph = [[0] * (maxV + 1) for _ in range(maxV + 1)]
    for edge in edges:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1

    global a
    a = 0
    def dfs(root, visited=[]):
        global a
        visited.append(root)

        for w in range(len(graph[root])):
            if graph[root][w] == 1 and (w not in visited):
                a += 1
                dfs(w, visited)

    for i in range(0, maxV + 1):
        dfs(i)
        print(a)

    answer = a

    return answer

solution(5, [[0,1],[0,2],[1,3],[1,4]])