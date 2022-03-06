import sys

###한 개의 정수를 입력받을 때
#n = int(sys.stdin.readline())

###정해진 개수의 정수를 한줄에 입력받을 때
#a, b = map(int, sys.stdin.readline().split())

###임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
#data = list(map(int,sys.stdin.readline().split()))


###임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
#data = []
#n = int(sys.stdin.readline())
#for i in range(n):
#    data.append(list(map(int,sys.stdin.readline().split())))

###문자열 n줄을 입력받아 리스트에 저장할 때
#import sys
#n = int(sys.stdin.readline())
#data = [sys.stdin.readline().strip() for i in range(n)]

def ABmodC(a, b, c):
    binb = bin(b)[2:]
    modc = [0]*len(binb)
    modc[0] = a%c
    for i in range(1, len(binb)):
        modc[i] = (modc[i-1]*modc[i-1])%c

    res = 1
    for i in range(len(binb)):
        if int(binb[-1-i]):
            res *= (modc[i])
            res %= c
    return res

x = ABmodC(5, 117, 19)
print(x)