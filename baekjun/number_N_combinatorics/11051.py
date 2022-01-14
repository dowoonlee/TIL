import sys

ult = 10007

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

n, k = map(int, sys.stdin.readline().split())
if n<2*k:
    k = n-k

denominator = [i+1 for i in range(k)]# 분모
numerater = [n-i for i in range(k)]# 분자


for i in range(k):
    for j in range(k):
        if numerater[i]==1:
            pass
        else:
            if denominator[j]>numerater[i]:
                gcd = GCD(denominator[j], numerater[i])
            else:
                gcd = GCD(numerater[i], denominator[j])
            denominator[j] /= gcd
            numerater[i] /= gcd

num = []
for i in numerater:
    if i!=1:
        num.append(int(i))

temp=1
temp_list=[]

for i in num:
    temp*=i
    if temp>1e7:
        temp_list.append(temp)
        temp=1

if len(temp_list)==0:
    print(int(temp%ult))

elif len(temp_list)==1:
    x = ((temp_list[0] % ult) * (temp % ult)) % ult
    print(int(x))

else:
    x = ((temp_list[0]%ult)*(temp_list[1]%ult)) % ult
    for i in range(len(temp_list)-2):
        x=(x * (temp_list[i+2]%ult)) % ult
    x = (x * (temp % ult)) % ult
    print(int(x))


