while True:
    words = input()
    if words == ".":
        break
    ans = 'yes'
    oc = []
    for s in words:
        if s == '(':
            oc.append(True)
        elif s == '[':
            oc.append(False)
        elif s == ')':
            if len(oc) == 0:
                ans = 'no'
                break
            else:
                if oc[-1]:#last open bracket is (=True
                    oc.pop()
                else:
                    ans = 'no'
                    break

        elif s == ']':
            if len(oc) == 0:
                ans = 'no'
            else:
                if not oc[-1]:#last open bracket is [=False
                    oc.pop()
                else:
                    ans = 'no'
                    break
        else:
            pass
    if len(oc) != 0:
        ans = 'no'
    print(ans)
