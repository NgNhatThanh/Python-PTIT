import math

def solve():
    n = int(input())
    print("1", end = '')
    for i in range(2, int(math.sqrt(n))):
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt > 0:
            print(" * " + str(i) + "^" + str(cnt), end = '')
    if n > 1:
        print(" * " + str(n) + "^1")
    else:
        print()
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()