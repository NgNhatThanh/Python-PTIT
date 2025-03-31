def solve():
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    res = 0
    for i in range(n - 2):
        l = i + 1
        r = n - 1
        while l < r:
            sum = lst[l] + lst[r] + lst[i]
            if sum == 0:
                res += 1
                l += 1
            elif sum > 0:
                r -= 1
            else:
                l += 1
    print(res)
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()

