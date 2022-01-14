import sys
import time
n = int(sys.stdin.readline())

t0 = time.time()
def diag(arr):
    if len(arr)<=1:
        i=1
        c=1
    else:
        c = 1
        i = 1
        while c and i < len(arr):
            j=0
            while j<i and c:
                c *= abs(arr[i] - arr[j]) - abs(i - j)
            i += 1
    return i-1, bool(c)#if c=False, 0~i-1 element is o.k


array = [i for i in range(n)]#0 ~ n-1
state = [False] * n

count = 0

#python으로는 불가능...



#print(time.time()-t0)
