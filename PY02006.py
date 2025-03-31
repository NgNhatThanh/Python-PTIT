def solve():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()
