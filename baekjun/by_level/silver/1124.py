import sys

a, b = map(int, sys.stdin.readline().split())

primes = [1]*(b+1)
primes[0] = 0
primes[1] = 0
for i in range(2, b+1):
    if primes[i]:
        j = 2
        while j * i <= b:
            primes[j*i] = 0
            j+=1
    else:
        pass

under_prime = primes[:]

for i in range(2, b+1):
    for j in range(2, b+1):
        if i * j > b:
            break
        elif primes[j]:
            under_prime[i*j] = under_prime[i] + 1

ans = 0
for i in range(a, b+1):
    if primes[under_prime[i]]:
        ans += 1

print(ans)





