import sys

n = int(sys.stdin.readline())
arr = [1]*13

for i in range(2, 13):
    arr[i] = arr[i-1]*i

print(arr[n])