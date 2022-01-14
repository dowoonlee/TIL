import sys

while True:
    try:
        a = sys.stdin.readline()
        x, y = map(int, a.split())
        print(x+y)
    except:
        break