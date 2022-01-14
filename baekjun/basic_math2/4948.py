import sys
n = int(sys.stdin.readline())
arr = [True]*(123456*2+1)
arr[0]=False
arr[1]=False

for i in range(2, int((123456*2)**(1/2))+1):
    if arr[i]:
        j=2
        while (i*j) <= 123456*2:
            arr[i*j] = False
            j+=1

while n:
    print(sum(arr[n+1:2*n+1]))
    n = int(sys.stdin.readline())
