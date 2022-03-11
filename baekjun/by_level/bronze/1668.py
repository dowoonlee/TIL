import sys

n = int(sys.stdin.readline())
t = [int(sys.stdin.readline()) for _ in range(n)]

def tcount(arr):
    maxh = 0
    count = 0
    for i in range(n):
        if arr[i]>maxh:
            maxh = arr[i]
            count += 1
        else:
            pass
    return count


print(tcount(t))
print(tcount(t[::-1]))



