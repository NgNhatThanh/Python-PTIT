def solve():
    s = input()
    bt, kq = s.split(" = ")
    kqd = eval(bt)
    if kqd == int(kq):
        print("YES")
    else:
        print("NO")
    return


def main():
    t = 1
    # t = int(input())
    for T in range(t):
        solve()
    return
main()