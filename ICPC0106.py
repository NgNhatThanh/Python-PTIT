def solve():
    b, s, res = int(input()), input(), []
    dec = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            dec += (1 << (len(s) - i - 1))
    if dec == 0:
        print(0)
    else:
        while dec > 0:
            rem = dec % b
            dec //= b
            if b == 16 and rem >= 10:
                rem = chr(rem - 10 + ord('A'))
            res.append(rem)
        for x in res[::-1]:
            print(x, end = '')
        print()
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()

