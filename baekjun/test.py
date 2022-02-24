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

def isfancy(x):## fancy or not
    count = [1,1]
    num = bin(x)[3:]
    ans = False
    for i in num:
        if int(i)==count[0]:
            count[1]+=1
        else:
            count[0] = int(i)
            count[1] = 1
        if count[1]>=3:
            ans = True
    return ans

x = 100
binx = bin(x)[2:]
print(binx)
xdigit = len(binx)

nf_dp = [0]*(xdigit+1)
nf_dp[0] = 1
nf_dp[1] = 1#모두 멋지지 않은 수
nf_dp[2] = 2**1#11, 10 모두 멋지지 않은 수
nf_dp[3] = 2**2-1#111만 멋진 수이므로 만들 수 있는 수에서 1개 빼기

for i in range(4, xdigit+1):
    nf_dp[i] = nf_dp[i-2]+2*nf_dp[i-3]+nf_dp[i-4]

dp = [0]*(xdigit+1)#0~n자리 이진수 중 멋진 수의 갯수
for i in range(1, (xdigit+1)):
    dp[i] = 2**(i-1)-nf_dp[i]+dp[i-1]

