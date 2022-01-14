import sys
n = int(sys.stdin.readline())
strn = str(n)
d = len(str(n))

arr = []
for i in strn:
    arr.append(int(i))
ans=''
for i in sorted(arr)[::-1]:
    ans+=str(i)
print(ans)
