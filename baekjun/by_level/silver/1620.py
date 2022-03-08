import sys

n, m = map(int, sys.stdin.readline().split())
pokename = dict()
pokenum = [""]*(n+1)

for i in range(n):
    pokemon = str(sys.stdin.readline().rstrip())
    pokename[pokemon] = i+1
    pokenum[i+1] = pokemon

for _ in range(m):
    qst = sys.stdin.readline().rstrip()
    try:
        print(pokenum[int(qst)])
    except ValueError:
        print(pokename[qst])
