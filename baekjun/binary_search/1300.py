import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
temp = []
for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        temp.append(i*j)
temp.sort()
print(temp)
print('Ans:', temp[k-1])

def ncount(x):#x보다 작거나 같 수들의 갯수를 return
    count = 0
    rowcut = min(x, n)
    for i in range(1, rowcut+1, 1):
        if i <= x:
            count += min(n, x//i)
    return count


start, end = 1, n**2
mid = (start+end)//2
count = ncount(mid)


while start<end:
    count = ncount(mid)
    print(start, mid, end, count)
    if count < k:
        print('c1')
        answer = mid
        start = mid + 1
    else:
        print('c2')
        end = mid
    mid = (start + end) // 2

print(start, mid, end)

check = True
while check:
    print(ncount(mid) ,ncount(mid-1))
    if ncount(mid) == ncount(mid-1):
        mid -= 1
    else:
        check=False
print(mid)