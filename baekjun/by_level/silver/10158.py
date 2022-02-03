import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

wr, hr = t%(2*w), t%(2*h)

p+=wr
q+=hr
if p>w:
    p = 2*w-p
if p<0:
    p=-p
if q>h:
    q = 2*h-q
if q<0:
    q=-q
print(p, q)


