import sys
w = str(sys.stdin.readline()).strip()

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
char0 = [i[0] for i in croa]
nchar = [len(i) for i in croa]

i = 0
l = 0
while i<len(w):
    check = False
    for j, char in enumerate(char0):
        if char==w[i] and len(w)-i>=nchar[j] and w[i:i+nchar[j]] == croa[j]:
            l+=1
            i+=nchar[j]
            check = True
            break
        else:
            pass
    if not check:
        l+=1
        i+=1
print(l)





