import sys

w = sys.stdin.readline().rstrip()
ans = ""
for st in w:
    if st.isupper():
        ans += st.lower()
    else:
        ans += st.upper()
print(ans)
