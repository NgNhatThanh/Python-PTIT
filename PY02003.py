maxN = 11000
dp = [0] * maxN
id2, id3, id5 = 0, 0, 0
dp[0] = 1

for i in range(1, maxN):
    dp[i] = min(dp[id2] * 2, dp[id3] * 3, dp[id5] * 5)
    if dp[i] == dp[id2] * 2:
        id2 += 1
    if dp[i] == dp[id3] * 3:
        id3 += 1
    if dp[i] == dp[id5] * 5:
        id5 += 1

def binSearch(n):
    l, r = 0, maxN - 1
    while l <= r:
        mid = (l + r) // 2
        if dp[mid] == n:
            return mid
        elif dp[mid] > n:
            r = mid - 1
        else:
            l = mid + 1
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    idx = binSearch(n)
    if idx == -1:
        print("Not in sequence")
    else:
        print(idx + 1)
