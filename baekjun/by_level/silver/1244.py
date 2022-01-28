import sys

n_switch = int(sys.stdin.readline())
states = list(map(int, sys.stdin.readline().split()))
#states = [0, 1, 0, 1, ...]
n_student = int(sys.stdin.readline())
for _ in range(n_student):
    gender, number = map(int, sys.stdin.readline().split())
    index = number - 1
    if gender-1:#female
        d, check = 0, True
        while check:
            if index+d>n_switch-1 or index-d<0:
                check = False
                break
            elif states[index + d] != states[index-d]:
                check = False
                break
            else:
                d+=1

        if d==0:
            states[index] = int(not(states[index]))
        else:
            d-=1
            for idx in range(index-d, index+d+1):
                states[idx] = int(not(states[idx]))
    else:#male
        i = 1
        while True:
            try:
                states[number*i-1] = int(not(states[number*i-1]))
            except IndexError:
                break
            i+=1
for i, v in enumerate(states):
    if not((i+1)%20):
        endment = '\n'
    else:
        endment = ' '
    print(i, end=endment)





