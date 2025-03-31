def solve():
    s = input()
    if len(s) == 1:
        print(s)
    else:
        lst = list(s)
        for i in range(len(lst) - 2, 0, -1):
            if ord(lst[i + 1]) >= ord('5') and ord(lst[i]) < ord('9'):
                lst[i] = chr(ord(lst[i]) + 1)
            lst[i + 1] = '0'
        if ord(lst[1]) >= ord('5'):
            if lst[0] == '9':
                lst[0] = "10"
            else:
                lst[0] = chr(ord(lst[0]) + 1)
        lst[1] = '0'
        for c in lst:
            print(c, end = '')
        print()
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()