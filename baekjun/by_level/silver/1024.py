import sys

N, L = map(int, sys.stdin.readline().split())

partial_sum = 0
size = 0
init_x=-1

for cur_len in range(L, 101):
    partial_sum = (cur_len**2 - cur_len)/2
    if not( (N-partial_sum)%cur_len ) and (N-partial_sum) // cur_len >=0:
        init_x = (N-partial_sum) / cur_len
        size = cur_len
        break

if init_x<0:
    print(-1)
else:
    for i in range(size):
        print(int(init_x+i), end=' ')




