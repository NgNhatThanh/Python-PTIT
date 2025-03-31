def solve():
    n = input()
    if len(n) >= 2 and n[0] == n[len(n) - 1]:
        print("YES")
    else:
        print("NO")
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()