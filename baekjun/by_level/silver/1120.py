import sys

a, b = map(str, sys.stdin.readline().split())

dl = len(b)-len(a)

listup = []

for i in range(dl+1):
    match = 0
    for j in range(len(a)):
        if a[j]==b[j+i]:
            match+=1
    listup.append(match + dl)


print(len(b)-max(listup))


