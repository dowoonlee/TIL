import sys
#n = int(sys.stdin.readline())
#age, name = [], []
#for i in range(n):
#    a, b = map(str, sys.stdin.readline().split())
#    age.append(int(a))
#    name.append(b)

#sign = [i for i in range(n)]

n = 3
age = [21, 21, 20]
name = ['Junkyu', 'Dohyun', 'Sunyoung']
sign = [0, 1, 2]

name_sign = []

for i in range(n):
    dummy = []
    dummy.append(age[i])
    dummy.append(sign[i])
    dummy.append(name[i])
    name_sign.append(dummy)

name_sign.sort(key=lambda x: (x[0], x[1]))
for i in range(n):
    print('%d %s'%(name_sign[i][0],name_sign[i][2]))