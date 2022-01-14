import sys


n, b = map(int, sys.stdin.readline().split())
a = []
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))


def mult(a, b):
    s = len(a)
    res = [[0]*s for i in range(s)]

    for i in range(s):
        for j in range(s):
            for k in range(s):
                res[i][j] += (a[i][k] * b[k][j]) % 1000
    return res


def nsq(a, n):
    s = len(a)

    if n == 1:
        return a

    elif n%2 == 0:
        sq_a = nsq(a, n//2)
        return mult(sq_a, sq_a)

    else:
        sq_a = nsq(a, n//2)
        return mult(a, mult(sq_a, sq_a))

answer = nsq(a, b)

for i in range(n):
    for j in range(n):
        print(answer[i][j]%1000, end=' ')
    print()