import math

def solve():
    n, x, m = list(map(float, input().split()))
    x /= 100
    res = math.ceil(math.log(m / n, 1 + x))
    print(res)
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()