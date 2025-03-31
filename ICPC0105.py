def solve():
    s = input()
    res = 0
    num = 0
    for x in s:
        if x.isdigit():
            num = num * 10 + ord(x) - 48
        else:
            res = max(res, num)
            num = 0
    res = max(res, num)
    print(res)
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()

