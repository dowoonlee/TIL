import sys
from itertools import combinations

n = int(sys.stdin.readline())
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
tree = sorted(tree, key=lambda x: x[2], reverse=True)

xcor = []
ycor = []

for i in range(n):
    xcor.append(tree[i][0])
    ycor.append(tree[i][1])

xcor = sorted(list(set(xcor)))
ycor = sorted(list(set(ycor)))


ans = 123456789
for td in range(len(ycor)):
    for tr in range(len(xcor)):
        for tu in range(len(ycor) - 1, td - 1, -1):
            for tl in range(len(xcor) - 1, tr - 1, -1):
                r = xcor[tr]
                l = xcor[tl]
                d = ycor[td]
                u = ycor[tu]
                perimeter = 2 * ((u - d) + (l - r))

                cnt, value = 0, 0
                valid = True


                for wood in tree:
                    if wood[1] < d or wood[1] > u or wood[0] < r or wood[0] > l:#outside=>cut
                        cnt += 1
                        value += wood[2]
                        if cnt >= ans:
                            valid = not valid#valid = False
                            break
                if not valid:#if valid==False
                    continue

                if perimeter <= value and cnt < ans:
                    ans = cnt
                    continue

                for wood in tree:#outside => cut tree in descending order
                    if wood[1] >= d and wood[1] <= u and wood[0] >= r and wood[0] <= l:
                        cnt += 1
                        value += wood[2]
                        if cnt >= ans:
                            valid = not valid
                            break
                        if value >= perimeter:
                            ans = cnt
                            break

print(ans)
