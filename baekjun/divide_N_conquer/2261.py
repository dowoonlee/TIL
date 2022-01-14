import sys

n = int(sys.stdin.readline())
pos = []
for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    pos.append((x, y))

pos.sort()

def d2(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def dnq(left, right):
    if left==right:
        return float('inf')
    else:
        mid = (left+right) // 2
        min_distance = min(dnq(left, mid), dnq(mid+1, right))
        target_list = []

        # 중간지점(mid)을 기준으로 좌측 탐색, min_distance보다 작을 때 까지만 target_list에 저장
        for i in range(mid, left-1, -1):
            if (pos[i][0]-pos[mid][0])**2 < min_distance:
                target_list.append(pos[i])
            else:
                break
        # 중간지점(mid)을 기준으로 측 탐색, min_distance보다 작을 때 까지만 target_list에 저장
        for j in range(mid + 1, right + 1):
            if (pos[j][0] - pos[mid][0]) ** 2 < min_distance:
                target_list.append(pos[j])
            else:
                break
        # x축 기준으로 sorting 된 pos를 저장한 target_list를 y축 기준으로 sorting
        target_list.sort(key=lambda x: x[1])

        for i in range(len(target_list) - 1):
            for j in range(i + 1, len(target_list)):
                if (target_list[i][1] - target_list[j][1]) ** 2 < min_distance:
                    dist = d2(target_list[i], target_list[j])
                    min_distance = min(min_distance, dist)
                else:
                    break
        return min_distance

if len(pos) != len(set(pos)):#같은 지점이 존재하
    print(0)
else:
    print((dnq(0, len(pos) - 1)))


