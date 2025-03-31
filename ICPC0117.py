def solve():
    se = set()
    n = int(input())
    for i in range(n):
        s = input()
        se.add(s)
    print(len(se))
    return


def main():
    t = 1
    # t = int(input())
    for T in range(t):
        solve()
    return
main()