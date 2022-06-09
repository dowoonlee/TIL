def comb(x, k):
    res = []
    if k == 0:
        return [[]]
    for i in range(0, len(x)):
        elem = x[i]
        rx = x[i + 1:]
        for C in comb(rx, k - 1):
            res.append([elem] + C)
    return res


for t in range(50):

    n = int(input())
    ans = input().rstrip()
    m = len(ans)
    stud = [input().rstrip() for _ in range(n)]

    arr = [[0] * len(ans) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = stud[i][j] == ans[j]


    flag = True
    std_case = [i for i in range(n)]
    nstd = 1
    while flag and nstd <= n:
        pick = comb(std_case, nstd)
        for p in pick:
            test_set = [False] * m
            for i in range(nstd):
                target = arr[p[i]]
                for j in range(m):
                    test_set[j] += target[j]
            t = 1
            for j in range(m):
                t *= test_set[j]
            if t > 0:
                flag = False
                break
        if flag:
            nstd += 1
    if nstd > n:
        print(-1)
    else:
        print(nstd)
