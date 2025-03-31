t = int(input())
for i in range(t):
    n = int(input())
    st = 1
    if n % 2 == 0:
        st = 2
    res = 0
    while st <= n:
        res += 1.0 / st
        st += 2
    print(f"{res:.6f}")