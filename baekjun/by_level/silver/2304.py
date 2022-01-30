import sys

n = int(sys.stdin.readline())
lh=[]
for i in range(n):
    lh.append(list(map(int, sys.stdin.readline().split())))

lh = sorted(lh, key=lambda l:l[1], reverse=True)#높이가 높은 순으로 정렬
l, h = [lh[i][0] for i in range(n)], [lh[i][1] for i in range(n)]

minl = min(l)#가장 왼쪽 좌표
heights = [0]*(max(l)-min(l)+1)#칸별 높이
h_uniq = sorted(list(set(h)), reverse=True)#중복되는 높이를 없애고 높은 순으로 정렬
left, right = l[0], l[0]#가장 높은 위치부터 시작(가장 높은 위치가 여러개여도 상관없음)

for i in range(len(h_uniq)):
    for j in range(n):
        if h[j] == h_uniq[i]:
            left, right = min(left, l[j]), max(right, l[j])
    for idx in range(left-minl, right-minl+1):
        if not(heights[idx]):#heights안에 0이 들어있다면
            heights[idx] = h_uniq[i]
print(sum(heights))








