import sys


n = int(sys.stdin.readline())
ns = list(map(int,sys.stdin.readline().split()))
ns.sort()
n_uniq = sorted(list(set(ns)))

n_dict = {}
i = 0
for j in n_uniq:
    count=0
    while i<n and ns[i] == j:
        count+=1
        i+=1
    n_dict[j] = count

m = int(sys.stdin.readline())
ms = list(map(int,sys.stdin.readline().split()))


def binaray_search(arr, x):
    st, ed = 0, len(arr)-1
    mid = int((st+ed)/2)
    while st<ed:
        if arr[mid]>x:
            ed = mid-1
        elif arr[mid]<x:
            st = mid+1
        else:
            return mid
        mid = int((st+ed)/2)

    return mid

for i in ms:
    try:
        sys.stdout.write('%d '%n_dict[i])
    except KeyError:
        sys.stdout.write('%d '%0)

#for i in range(m):
#    pos = binaray_search(n_uniq, ms[0])
#    print(n_dict[pos], end=' ')

