import sys

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

stack = [0]#data의 수를 저장하지 않고 data내 index를 저장
ans = [-1]*n#NGE가 없을 땐 자동으로 -1

i = 1
while stack and i<n:#stack이 비어있지 않고, data의 마지막까지 계산
    while stack and data[stack[-1]] < data[i]:#stack이 비어있지 않고 stack의 top이 현재 data보다 작다면
        ans[stack[-1]] = data[i]#stack에 top index에 대응되는 NGE는 현재 data의 위치인 data[i]
        stack.pop()# i-1번째 (stack의 top)의 NGE를 계산했으니 stack의 top을 빼냄
    stack.append(i)#stack에 index 저장
    i += 1#다음번 data로 이동

for i in range(n):
    print(ans[i], end=" ")
