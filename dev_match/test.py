import sys
#n = int(sys.stdin.readline())


def test(n):
    d = 4
    dd = 20
    while dd<=n:
        d+=1
        dd += (d-3)*(9**(d-4)*10) + 10**(d-3)

    d_add = d-3
    add = ['%05d'%i for i in range(10**d_add)]



    sixes = []
    for i in add:
        sixes.append(int(i+'666'))
        for j in range(len(i)):
            sixes.append(int(i[0:j]+'666'+i[j::]))
    sixes = sorted(list(set(sixes)))
    for i in range(200):
        print(i+1,":", sixes[i])
    return

test(21)