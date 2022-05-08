import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = str(sys.stdin.readline().rstrip())


def LPS(word):
    arr = [0] * len(word)
    j = 0
    for i in range(1, len(word)):
        while j > 0 and word[i] != word[j]:
            j = arr[j - 1]
        if word[i] == word[j]:
            j += 1
            arr[i] = j
    return arr


def kmp(word):
    lps = LPS(word)
    cnt = 0
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != word[j]:
            j = lps[j - 1]
        if s[i] == word[j]:
            if j == len(word) - 1:
                cnt += 1
                j = lps[j]
            else:
                j += 1
    return cnt


ans = kmp("IO" * n + "I")
print(ans)
