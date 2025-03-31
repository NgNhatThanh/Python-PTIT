t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    st = []
    left = [0] * n
    for i in range(n):
        while len(st) > 0 and lst[st[len(st) - 1]] <= lst[i]:
            st.pop()
        if len(st) == 0:
            left[i] = -1
        else:
            left[i] = st[len(st) - 1]
        st.append(i)
    for i in range(n):
        print(i - left[i], end = ' ')
    print()