import sys

n = int(sys.stdin.readline())
vote = [int(sys.stdin.readline()) for _ in range(n)]


if n<2:
    print(0)

else:
    ds, rest = vote[0], vote[1::]
    ans=0
    while max(rest)>=ds:
        ds += 1
        rest[rest.index(max(rest))] -= 1
        ans+=1
    print(ans)


