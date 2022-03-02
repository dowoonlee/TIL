import sys

n, r, c = map(int, sys.stdin.readline().split())


def quad(arr):
    ri, re, ci, ce = arr[0], arr[1], arr[2], arr[3]
    nquad = ((re - ri) + 1) * ((ce - ci) + 1) // 4


    if r <= (ri + re) // 2 and c <= (ci + ce) // 2:  # 1st quad
        return [ri, (ri + re) // 2, ci, (ci + ce) // 2], 0

    elif r <= (ri + re) // 2 and c > (ci + ce) // 2:  # 2nd quad
        return [ri, (ri + re) // 2, (ci + ce) // 2 + 1, ce], nquad

    elif r > (ri + re) // 2 and c <= (ci + ce) // 2:  # 3rd quad
        return [(ri + re) // 2 + 1, re, ci, (ci + ce) // 2], nquad * 2

    else:
        return [(ri + re) // 2 + 1, re, (ci + ce) // 2 + 1, ce], nquad * 3


coord = [0, 2 ** n - 1, 0, 2 ** n - 1]
ans = 0
while (coord[0] != coord[1]):
    coord, ad = quad(coord)
    ans += ad

print(ans)
