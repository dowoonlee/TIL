import sys

#n = int(sys.stdin.readline())

#arr = [int(sys.stdin.readline()) for _ in range(n)]
#arr = [4, 3, 6, 8, 7, 5, 2, 1]
arr = [1,2,5,3,4]

def stack_solver(xs):
    stack = []
    i = 0
    q = 1
    ans = ''
    while i < len(xs):
        if len(stack)==0: #if stack is empty
            stack.append(q)
            ans += '+'
            q += 1

        else: #if stack is not empty
            if stack[-1] != xs[i]:
                if q <= xs[i]:
                    stack.append(q)
                    ans += '+'
                    q += 1
                else:#current adding number(q) is g.t. than series(xs[i])
                    return ['NO']

            else:
                stack.pop()
                ans += '-'
                i += 1
    return ans

for i in stack_solver(arr):
    print(i)