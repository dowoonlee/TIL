import sys
n = int(sys.stdin.readline())

if n < 100:
    print(n)

elif n==1000:
    print(144)


else:
    ans=[]
    count = 0
    for i in range(1, n//100+1):
        x = [i, 0, 0]
        d = -int(i//2)
        x[1], x[2] = x[0] + d, x[0] + 2 * d
        dcond = True

        while x[2] + 10*x[1] + 100*x[0] <= n and dcond:
            if i+2*d>=10 or i+2*d<0:
                dcond=False
            else:
                count += 1
            d += 1
            x[1], x[2] = x[0]+d, x[0]+2*d
    print(99+count)

