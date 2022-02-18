import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a_d, b_d = [0]*4, [0]*4
    a_list = list(map(int, sys.stdin.readline().split()))
    for ad in a_list[1:]:
        a_d[ad-1] += 1
    b_list = list(map(int, sys.stdin.readline().split()))
    for bd in b_list[1:]:
        b_d[bd-1] += 1

    end = False
    for i in range(3, 0, -1):
        if a_d[i]>b_d[i]:
            print('A')
            end=True
            break
        elif a_d[i]<b_d[i]:
            print('B')
            end=True
            break
        else:
            pass
    if not end:
        if a_d[0]>b_d[0]:
            print('A')
        elif a_d[0]<b_d[0]:
            print('B')
        else:
            print('D')

