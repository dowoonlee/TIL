ans = 0
for i in range(1, 1000):
    if not(i%2) and not(i%7):
        ans+=i
print(ans)
