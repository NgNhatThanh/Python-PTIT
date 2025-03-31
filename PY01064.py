def solve(n, k):
    if k == (1 << n):
        return chr(ord('A') + n)
    if k > (1 << n):
        return solve(n - 1, k - (1 << n))
    return solve(n - 1, k)

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    print(solve(n, k))