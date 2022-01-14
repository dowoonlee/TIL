import sys

ipt = str(sys.stdin.readline().rstrip())

stack = []
l = 0
tmp = ''

for c in ipt:
    if c.isdigit():
        l += 1
        tmp = c
    elif c == '(':
        stack.append((tmp, l-1))
        l=0
    else:
        multi, preL = stack.pop()
        l = (int(multi) * l ) + preL

print(l)

