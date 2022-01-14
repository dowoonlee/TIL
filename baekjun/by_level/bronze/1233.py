import sys

s1, s2, s3 = map(int, sys.stdin.readline().split())
eyes = [0]*(s1+s2+s3)
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            eyes[i+j+k-1] += 1
print(eyes)
print(eyes.index(max(eyes))+1)