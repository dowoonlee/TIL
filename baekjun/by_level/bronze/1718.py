import sys

letter = str(sys.stdin.readline().rstrip())
keys = str(sys.stdin.readline().rstrip())

ans = ''
k_idx = -1
for i in range(len(letter)):
    if k_idx == len(keys)-1:
        k_idx = 0
    else:
        k_idx += 1
    if letter[i]==' ':
        ans+=' '
    else:
        new_word = ord(letter[i])-(ord(keys[k_idx])-ord('a')+1)
        if new_word<ord('a'):
            new_word += 26
        ans += chr(new_word)
print(ans)

