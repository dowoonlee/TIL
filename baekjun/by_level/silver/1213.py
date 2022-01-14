import sys

name = str(sys.stdin.readline().rstrip())
name_list = list(name)
alphabet = sorted(list(set(name)))
number = [0]*len(alphabet)

for n in name:
    for i, a in enumerate(alphabet):
        if n==a:
            number[i]+=1
odd=1
for i, v in enumerate(number):
    if v%2!=0:
        odd-=1
        oddkey = i

answer=''
if odd<0:
    answer += "I'm Sorry Hansoo"

elif odd == 1:
    tans = ''
    for i, v in enumerate(number):
        tans += alphabet[i] * int((v / 2))
    answer = tans + tans[::-1]

else:
    number[oddkey] -= 1
    tans=''
    for i, v in enumerate(number):
        tans += alphabet[i] * int((v/2))
    answer = tans + alphabet[oddkey] + tans[::-1]

print(answer)

