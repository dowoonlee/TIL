import sys

n = int(sys.stdin.readline())
std_id = [0]*n

for i in range(n):
    std_id[i] = int(sys.stdin.readline())

k = 1
test_id = [0]*n
for i in range(n):
    test_id[i] = std_id[i]%(10**k)
while (n!=len(set(test_id))):
    k+=1
    for i in range(n):
        test_id[i] = std_id[i] % (10 ** k)
print(k)
