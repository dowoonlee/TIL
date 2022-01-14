import sys
t = sys.stdin.readline()


arr = [True]*(10000*2+1)
arr[0]=False
arr[1]=False
for i in range(2, int((10000)**(1/2))+1):
    if arr[i]:
        j=2
        while (i*j) <= 10000:
            arr[i*j] = False
            j+=1
for i in range(int(t)):
    n = int(sys.stdin.readline())
    rg = int(n/2)
    for j in range(n-1):
        if (arr[rg-j] and arr[rg+j]):
            print(rg-j, rg+j)
            break