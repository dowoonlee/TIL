import sys

#n = int(sys.stdin.readline())
#a = list(map(int,sys.stdin.readline().split()))
#n, a = 6, [10, 20, 10, 30, 20, 50]
n, a = 7, [7, 2, 9, 10, 3, 8, 10]

def lower_bound(arr, x):
    ans = 0
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > x:  # (left, mid-1) / mid is bigger than answer
            right = mid - 1
        else:  # (mid+1, right)
            left = mid + 1
            ans = mid
    if arr[ans]<x:
        ans+=1
    return ans


temp = [1,3,5,7,9]
x = lower_bound(temp, 3)
print(x, temp[x])


stack = []
for i in range(len(a)):
    print(i, stack, a[i])
    if not stack:#when the stack is empty
        stack.append(a[i])

    else:
        if stack[-1]<a[i]:
            stack.append(a[i])
        else:
            pos = lower_bound(stack, a[i])
            stack[pos] = a[i]

print(stack)