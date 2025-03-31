def solve():
    c = [str(x) for x in input().split()]
    list = [str(x) for x in input().split()]
    x1, x2 = list[0], ''
    if len(list) == 1:
        x2 = input()
    else: x2 = list[1]

    if c[0] > c[1]:
        c[0], c[1] = c[1], c[0]

    minX1 = x1.replace(c[1], c[0])
    minX2 = x2.replace(c[1], c[0])

    maxX1 = x1.replace(c[0], c[1])  
    maxX2 = x2.replace(c[0], c[1])

    print(int(minX1) + int(minX2), end = ' ')
    print(int(maxX1) + int(maxX2))
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()

