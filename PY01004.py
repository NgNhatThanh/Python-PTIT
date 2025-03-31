import math

def solve():
    n = int(input())
    cnt = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            cnt += 1
    if check(cnt):
        print("YES")
    else:
        print("NO")
    return

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()