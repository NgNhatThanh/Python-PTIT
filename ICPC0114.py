import math

def solve():
    n = int(input())
    rev = int(str(n)[::-1])
    cs = tongcs(n)
    if check(n) and check(rev) and (check(cs)):
        while n > 0:
            c = n % 10
            if c != 2 and c != 3 and c != 5 and c != 7:
                print("No")
                return
            n //= 10
        print("Yes")
    else:
        print("No")
    return

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def tongcs(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def main():
    t = 1
    t = int(input())
    for T in range(t):
        solve()
    return
main()