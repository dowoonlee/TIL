
limit = 10000
arrs = [True for _ in range(limit)]



def selfnumber(n):
    ans = n
    for i in str(n):
        ans += int(i)
    return ans

for i in range(limit):
    sn = selfnumber(i+1)
    if sn <= limit:
        arrs[sn-1] = False
    if arrs[i]:
        print(i+1)




