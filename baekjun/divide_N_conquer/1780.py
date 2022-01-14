import sys
n = int(sys.stdin.readline())

data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

ans = [0, 0, 0]#0, 1, -1

def cutt(image):
    global ans

    s3 = int(len(image)/3)

    lst = [i for i in range(s3)]

    for i in range(3):
        for j in range(3):
            timage = [image[i * s3:(i + 1) * s3][k][j * s3:(j + 1) * s3] for k in lst]
            k1, k2 = 0, 0
            zok = True
            while k1 < s3 and zok:
                if len(set(timage[k1])) != 1 or list(set(timage[k1]))[0]!=timage[0][0]:
                    zok = False
                    break
                k1+=1
            if zok:#all the same
                ans[timage[0][0]]+=1
            else:
                cutt(timage)

if sum(map(sum, data))==len(data)**2:
    print(0)
    print(0)
    print(1)
elif sum(map(sum, data))==-len(data)**2:
    print(1)
    print(0)
    print(0)
else:
    k1, k2 = 0, 0
    zok = True
    while k1<len(data) and zok:
        for k2 in range(len(data)):
            if data[k1][k2]:
                zok= False
                break
        k1+=1
    if zok:
        print(0)
        print(1)
        print(0)
    else:
        cutt(data)
        print(ans[-1])
        print(ans[0])
        print(ans[1])
