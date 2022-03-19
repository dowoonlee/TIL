# 문제 설명
# 트리 tree_a와 트리 tree_b가 주어집니다.
# tree_a는 n개의 정점으로 이루어져 있고 각 정점들은 1~n 번호를 겹치지 않게 가지고 있습니다.
# tree_b도 n개의 정점으로 이루어져 있고 각 정점들은 1~n 번호를 겹치지 않게 가지고 있습니다.
#
# 당신은 tree_b를 tree_a와 똑같이 만들고 싶습니다.
#
# 당신은 두 가지 작업을 할 수 있습니다.
#
# tree_b에 존재하는 간선 하나를 삭제하고 새로운 간선 하나를 추가합니다.
# tree_b에 존재하는 두 정점의 번호를 바꿉니다.
# 1번 작업은 무제한으로 할 수 있지만 2번 작업은 최대 m번까지 밖에 할 수 없습니다.
#
# tree_a의 간선 정보를 담고 있는 2차원 정수 배열 a, tree_b의 간선 정보를 담고 있는 2차원 정수 배열 b, 2번 작업을 할 수 있는 횟수 m이 매개변수로 주어집니다. 이때, tree_b를 tree_a와 똑같이 만들기 위해 해야 하는 1번 작업의 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 1 ≤ a의 길이 = b의 길이 ≤ 12
# a의 원소는 [x, y] 형태이며, tree_a에서 x번 정점과 y번 정점이 양방향 간선으로 연결되어 있다는 뜻입니다.
# b의 원소는 [x, y] 형태이며, tree_b에서 x번 정점과 y번 정점이 양방향 간선으로 연결되어 있다는 뜻입니다.
# 1 ≤ x, y ≤ 1 + a의 길이
# x ≠ y
# 동일한 간선에 대한 정보가 중복해서 주어지지 않습니다.
# 항상 하나의 트리 형태로 입력이 주어지며, 잘못된 데이터가 주어지는 경우는 없습니다.
# tree_a의 정점 갯수, tree_b의 정점 갯수 = 1 + a의 길이
# 0 ≤ m ≤ 3

#a, b, m = [[1, 2], [2, 3]], [[1, 3], [3, 2]], 1
#a, b, m = [[1, 2], [3, 1], [2, 4], [3, 5]], [[2, 1], [4, 1], [2, 5], [3, 2]],1
#a, b, m = [[3, 4], [7, 2], [5, 4], [2, 3], [6, 5], [1, 2]], [[2, 1], [3, 6], [1, 4], [1, 5], [7, 1], [3, 2]],2

def solution(a, b, m):
    a.sort()
    b.sort()

    node_n = len(a)+1
    tree_a = [[0]*(node_n+1) for _ in range(node_n+1)]
    tree_b = [[0] * (node_n + 1) for _ in range(node_n + 1)]

    for node_a in a:
        tree_a[node_a[0]][node_a[1]] = 1
        tree_a[node_a[1]][node_a[0]] = 1

    for node_b in b:
        tree_b[node_b[0]][node_b[1]] = 1
        tree_b[node_b[1]][node_b[0]] = 1


    def searcha(i):
        for row in node_n:
            if tree_a[row][i]:
                return row

    def mth(i, j):
        tree_b[i[0]][i[1]] = 0
        tree_b[i[1]][i[0]] = 0
        tree_b[j[0]][j[1]] = 1
        tree_b[j[1]][j[0]] = 1


    init = 1

    answer = 0
    return answer


x = solution(a, b, m)
print(x)