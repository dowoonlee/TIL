import sys
n = int(sys.stdin.readline())

def func(arr, x):
    if x[0]=='push':
        arr.append(int(x[1]))
    elif x[0] == 'pop':
        if len(arr):
            print(arr.pop())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(arr))
    elif x[0] == 'empty':
        if len(arr):
            print(0)
        else:
            print(1)
    else:
        if len(arr):
            print(arr[-1])
        else:
            print(-1)
    return arr

stack = []
for i in range(n):
    data = list(map(str, sys.stdin.readline().split()))
    stack = func(stack, data)