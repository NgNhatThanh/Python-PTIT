t = int(input())
for _ in range(t):
    s = input()
    st = []
    res = []
    cnt = 1
    for i in range(len(s)):
        if s[i] == '(':
            st.append(cnt)
            res.append(cnt)
            cnt += 1
        elif s[i] == ')':
            res.append(st[-1])
            st.pop()
    print(*res)