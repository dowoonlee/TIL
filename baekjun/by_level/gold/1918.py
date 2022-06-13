import sys

ipt = sys.stdin.readline().rstrip()


def isOper(x):
    oper = "(*/+-)"
    for i in oper:
        if i == x:
            return True
    return False


