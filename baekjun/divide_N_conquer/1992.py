import sys


n = int(sys.stdin.readline())

data = []
for i in range(n):
    tdata = sys.stdin.readline().split()[0]
    tlist = []
    for j in tdata:
        tlist.append(int(j))
    data.append(tlist)

z = ""


def qt(image):
    global z
    z+="("
    size = len(image)
    lst = [i for i in range(int(size / 2))]

    for i in range(2):
        for j in range(2):
            qimage = [image[i * int(size / 2):(i + 1) * int(size / 2)][k][j * int(size / 2):(j + 1) * int(size / 2)] for k in lst]
            if sum(map(sum, qimage))==(size**2/4):
                z+="1"
            elif sum(map(sum, qimage))==0:
                z+="0"
            else:
                qt(qimage)
    z+=")"

if sum(map(sum, data))==len(data)**2:
    print(1)
elif sum(map(sum, data))==0:
    print(0)
else:
    qt(data)
    print(z)