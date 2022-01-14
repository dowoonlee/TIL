import sys

n = int(sys.stdin.readline())
ns = list(map(int,sys.stdin.readline().split()))
ns.sort()

m = int(sys.stdin.readline())
ms = list(map(int,sys.stdin.readline().split()))


def binaray_search(arr, x):
    st, ed = 0, len(arr)-1
    mid = int((st+ed)/2)
    while st<ed:
        print('st:',st,' ed:', ed)
        if arr[mid]>x:
            ed = mid-1
        elif arr[mid]<x:
            st = mid+1
        else:
            return 1
        mid = int((st+ed)/2)

    return int(x in arr[st:ed+1])


for i in range(m):
    print(binaray_search(ns, ms[i]))







