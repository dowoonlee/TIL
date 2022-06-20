import sys

ipt = list(sys.stdin.readline().rstrip())


def isOper(x):
    oper = "(*/+-)"
    for i in oper:
        if i == x:
            return True
    return False


opMap = dict()
opMap["*"] = 3
opMap["/"] = 3
opMap["+"] = 2
opMap["-"] = 2
opMap["("] = 1

operator = []
total = []

idx = 0
while idx < len(ipt):
    isOp = isOper(ipt[idx])
    if isOp:
        opX = ipt[idx]
        if len(operator) == 0 or opX == "(":
            operator.append(ipt[idx])
        elif opX == ")":
            temp = "1"
            while temp[0] != "(":
                temp = operator.pop()
                total.append(temp)
            total.pop()
        else:
            temp = operator[-1]
            while opMap[temp] >= opMap[opX] and operator and temp[0] != "(":
                total.append(operator.pop())
                if len(operator) < 1:
                    break
                else:
                    temp = operator[-1]
            operator.append(opX)
        idx += 1
    else:
        if idx == len(ipt) - 1:
            total.append(ipt[idx])
            idx+=1
        else:
            j = idx
            temp_isOp = False
            while not temp_isOp and j < len(ipt):
                temp_isOp = isOper(ipt[j])
                j += 1
            for i in range(idx, j-1):
                total.append(ipt[i])
            idx = j-1
while operator:
    total.append(operator.pop())

print("".join(total))
