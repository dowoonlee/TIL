import sys

n, m = map(int, sys.stdin.readline().split())
a = []
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))


m, k = map(int, sys.stdin.readline().split())
b = []
for i in range(m):
    b.append(list(map(int,sys.stdin.readline().split())))

n2size = 1
n2cut = max([n,m,k])
while n2size<n2cut:
    n2size*=2


def make_square_matrix(mat, n2):
    row, col = len(mat), len(mat[0])
    res = [[0]*n2 for i in range(n2)]
    for i in range(row):
        for j in range(col):
            res[i][j] = mat[i][j]
    return res

a2 = make_square_matrix(a, n2size)
b2 = make_square_matrix(b, n2size)

def mat_sub(matA, matB):
    size = len(matA)
    matC = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            matC[i][j] = (matA[i][j] - matB[i][j])
    return matC

def mat_sum(matA, matB):
    size = len(matA)
    matC = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            matC[i][j] = (matA[i][j] + matB[i][j])
    return matC


def strassen_matrix(matA, matB):

    s = len(matA)

    matC = [[0]*s for i in range(s)]

    if s==1:
        matC[0][0] = matA[0][0] * matB[0][0]
        return matC

    else:
        s2 = int(s / 2)
        A11 = [matA[0:int(s2)][k][0:int(s2)] for k in [i for i in range(int(s2))]]
        A12 = [matA[0:int(s2)][k][int(s2)::] for k in [i for i in range(int(s2))]]
        A21 = [matA[int(s2)::][k][0:int(s2)] for k in [i for i in range(int(s2))]]
        A22 = [matA[int(s2)::][k][int(s2)::] for k in [i for i in range(int(s2))]]

        B11 = [matB[0:int(s2)][k][0:int(s2)] for k in [i for i in range(int(s2))]]
        B12 = [matB[0:int(s2)][k][int(s2)::] for k in [i for i in range(int(s2))]]
        B21 = [matB[int(s2)::][k][0:int(s2)] for k in [i for i in range(int(s2))]]
        B22 = [matB[int(s2)::][k][int(s2)::] for k in [i for i in range(int(s2))]]

        M1 = strassen_matrix(mat_sum(A11, A22), mat_sum(B11, B22))
        M2 = strassen_matrix(mat_sum(A21, A22), B11)
        M3 = strassen_matrix(A11, mat_sub(B12, B22))
        M4 = strassen_matrix(A22, mat_sub(B21, B11))
        M5 = strassen_matrix(mat_sum(A11, A12), B22)
        M6 = strassen_matrix(mat_sub(A21, A11), mat_sum(B11, B12))
        M7 = strassen_matrix(mat_sub(A12, A22), mat_sum(B21, B22))

        C11 = mat_sum(mat_sub(mat_sum(M1, M4), M5), M7)
        C12 = mat_sum(M3, M5)
        C21 = mat_sum(M2, M4)
        C22 = mat_sum(mat_sum(mat_sub(M1, M2), M3), M6)

        for i in range(s2):
            for j in range(s2):
                matC[i][j] = C11[i][j]
                matC[i][j+s2] = C12[i][j]
                matC[i+s2][j] = C21[i][j]
                matC[i+s2][j+s2] = C22[i][j]

        return matC



c = strassen_matrix(a2, b2)

for i in range(n):
    for j in range(k):
        print(c[i][j], end=' ')
    print()

