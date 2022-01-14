import sys

ohm = {'black':0,
      'brown': 1,
      'red' : 2,
      'orange': 3,
      'yellow': 4,
      'green': 5,
      'blue': 6,
      'violet':7,
      'grey':8,
      'white': 9}

ans = ''
for _ in range(2):
    ipt = str(sys.stdin.readline().rstrip())
    ans+=str(ohm[ipt])
last = int(ohm[sys.stdin.readline().rstrip()])
ans = int(ans)*(10**last)
print(ans)


