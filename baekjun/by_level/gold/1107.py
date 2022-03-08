import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
if m>0:
    ooo = list(map(int, sys.stdin.readline().split()))

    nup, ndown = n * 1, n * 1
    condup, conddown = True, True
    while condup and conddown:
        nup += 1
        ndown -= 1
        nupstr = str(nup)
        ndownstr = str(ndown)
        countup = 0
        countdown = 0
        for o in ooo:
            countup += (str(o) in nupstr)
            countdown += (str(o) in ndownstr)
        if countup == 0:
            condup = False
        if countdown == 0:
            conddown = False

    if condup:
        difn = ndown
    else:
        difn = nup

    ans1 = abs(difn - n) + len(str(difn))
    ans2 = abs(n - 100)
    print(min(ans1, ans2))

else:
    ans1 = len(str(n))
    ans2 = abs(n - 100)
    print(min(ans1, ans2))