import math

def solve():
    n = int(input())
    tmp = n
    sum = 0
    while tmp > 0:
        sum += math.factorial(tmp % 10)
        tmp //= 10
    if sum == n:
        print("Yes")
    else:
        print("No")
    return


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()