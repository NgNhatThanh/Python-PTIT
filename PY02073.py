t = int(input())
for _ in range(t):
    n = int(input())
    x, y, z = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + x
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + z, dp[(i // 2) + 1] + y + z)
        else:
            dp[i] = min(dp[i], dp[i // 2] + x + z, dp[(i + 1) // 2] + y + z)
    print(dp[n])