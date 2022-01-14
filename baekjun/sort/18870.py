"""
import sys
n = int(sys.stdin.readline())

x = list(map(int, sys.stdin.readline().split()))

uniq = sorted(list(set(x)))
ans = ''
for i in range(n):
    ans += ' %d'%(uniq.index(x[i]))
print(ans)
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
x = list(map(int, input().split()))
uniq = sorted(set(x))
uniq_dict={i:v for v,i in enumerate(uniq)}
for i in x:
    print(f'{uniq_dict[i]} ')