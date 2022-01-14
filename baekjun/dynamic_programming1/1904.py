import sys
import time

for n in range(1, 1000001):
#n = int(sys.stdin.readline())
    print(n)
    #t0 = time.time()
    ult = 15746


    fib = [0]*max(n+1, 3)
    fib[1] = 1
    fib[2] = 2

    for i in range(3, n+1):
        fib[i] = (fib[i-1]+fib[i-2])%ult

    #print(fib[n])





#print(time.time()-t0 < 0.75)

