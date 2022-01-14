import sys
import re

t = int(sys.stdin.readline())

for _ in range(t):
    case = str(sys.stdin.readline().rstrip())
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(case)
    print('YES' if m else 'NO')




