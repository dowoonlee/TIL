import sys

l, r = map(int, sys.stdin.readline().split())
lbin, rbin = bin(l)[2:], bin(r)[2:]

ldigit, rdigit = len(bin(l))-2, len(bin(r))-2
print(lbin, rbin)

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



# let f(n) = n자리 이진수 중 멋지지 않은 수 라 할 때, n자리 이진수는 무조건 1로 시작
# 1-10-1-  f(n-3)
#     -01- f(n-4)
#  -0-01-  f(n-3)
#    -1-   f(n-2)

nf_dp = [0]*(rdigit+1)
nf_dp[0] = 1
nf_dp[1] = 1#모두 멋지지 않은 수
nf_dp[2] = 2**1#11, 10 모두 멋지지 않은 수
nf_dp[3] = 2**2-1#111만 멋진 수이므로 만들 수 있는 수에서 1개 빼기

for i in range(4, rdigit+1):
    nf_dp[i] = nf_dp[i-2]+2*nf_dp[i-3]+nf_dp[i-4]

dp = [0]*(rdigit+1)#n자리 이진수 중 멋진 수의 갯수
for i in range(1, (rdigit+1)):
    dp[i] = 2**(i-1)-nf_dp[i]


def same_digit_but_small(x):
    xbin = bin(x)[2:]
    xdigit = len(xbin)
    xdeci_max = 2**xdigit-1
    xdeci_min = 2**(xdigit-1)
    n_fancy = 0
    if xbin[0:3]=="111":
        n_fancy = xdeci_max-x

    elif xbin[0:3]=="110":
        if xbin[3:5]=="00":
            n_fancy = x-xdeci_min+1
        elif xbin[3:5]=="01":
            n_fancy = 2**(xdigit-5) + dp[xdigit-2] + dp[xdigit-3] + 2**(xdigit-4)
            n_fancy = dp[xdigit-4] + 2**(xdigit-5) + dp[xdigit-2] + dp[xdigit-3] + 2**(xdigit-4)
            #11001~ + 11000~ + 1101~ + 1001~ + 1000~
        else:#xbin[3] == 1
            n_fancy = dp[xdigit-3] + 2**(xdigit-5) + dp[xdigit-4] + dp[xdigit-3] + dp[xdigit-2] + 2**(xdigit-4)
            #1101~

    else:#10~
        if xbin[2:4]=="00":
            n_fancy = x-xdeci_min+1
        elif xbin[2:4]=="01":
            n_fancy = dp[xdigit-3] + 2**(xdigit-4)
            # 1001~ + 1000~
        else:
            n_fancy = dp[xdigit-2] + 2**(xdigit-4) + dp[xdigit-3]
            #101~ + 1000~ + 1001~
    return n_fancy





#X = dp[rdigit-1] + (r자리 fancy# 중 r보다 작은 애들)
#Y = dp[ldigit-1] + (l자리 fancy# 중 l보다 작은 애들)
#ans = X-Y

rightside = sum(dp[0:rdigit]) + same_digit_but_small(r) + isfancy(r)
print(rightside)
leftside = sum(dp[0:ldigit]) + same_digit_but_small(l)
print('L',leftside)
count = 0
realcount = []
for i in range(l, r+1):
    count+=isfancy(i)
    if i==l or i==r:
        realcount.append(count)
print(count)
#print("%d+%d=%d(%d)"%(dp[ldigit-1], same_digit_but_small(l), leftside, realcount[0]))
#print("%d+%d=%d(%d)"%(dp[rdigit-1], same_digit_but_small(r), rightside, realcount[1]))



#print("%d+%d-(%d+%d)+%d"%(dp[rdigit-1], same_digit_but_small(r), dp[ldigit-1], same_digit_but_small(l), int(isfancy(l))))
print(rightside-leftside)

