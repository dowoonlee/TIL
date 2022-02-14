n = int(input())

n3 = []
for i in range(9):
    n3.append(i*3)

n_sub=[n-j for j in n3]
n_sub_f = [j for j in n_sub if j>=0]
n_sub_f5 = [j%5 for j in n_sub_f]

print(n_sub)
print(n_sub_f)
print(n_sub_f5)

try:
    idx = n_sub_f5.index(0)
    fives = (n-(idx*3))//5
    threes = idx
    print(fives+threes)
except ValueError:
    print(-1)