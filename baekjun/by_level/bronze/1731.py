import sys

n = int(sys.stdin.readline())
an = [int(sys.stdin.readline()) for _ in range(n)]


def f1(arr):
    d = arr[1] - arr[0]
    flag = True
    for i in range(1, len(arr) - 1):
        if d != arr[i + 1] - arr[i]:
            flag = False
            break
    return flag


if f1(an):
    print(an[-1] + an[1] - an[0])
else:
    print(an[-1] * (an[1] // an[0]))
