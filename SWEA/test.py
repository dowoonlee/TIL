import sys
import numpy as np
import matplotlib.pyplot as plt

f = open("C:/Users/my/Downloads/input.txt",'r')
t = int(f.readline())
for i in range(2):
    n = int(f.readline())
    a = f.readline()
    a = list(map(int, a.split(" ")))
    l = 0
    cost = 0
    count = 0
    while l<n-1 and count<10:
        print(a[l:], l)
        maxv_ind = np.where(a[l:])[0][0]
        for j in range(l, maxv_ind):
            cost -= a[j]
        cost += (maxv_ind-l)*a[maxv_ind]
        l = maxv_ind+1
        count+=1
    print(i+1, cost)
f.close()



