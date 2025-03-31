def solve():
    s = input()
    res = int(1e18)
    num = 0
    for x in s:
        if x.isdigit():
            num = num * 10 + ord(x) - 48
        else:
            if num > 0:
                res = min(res, num)
            num = 0
    if num > 0:
        res = min(res, num)
    print(res)
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()

