import sys
import math

N, kim, lim = map(int, sys.stdin.readline().split())
i=1
while math.ceil(kim/2) != math.ceil(lim/2):
	kim = math.ceil(kim/2)
	lim = math.ceil(lim/2)
	i+=1
print(i)






