import math
from itertools import permutations

t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(i + 1)
    print(math.factorial(n))
    res = []
    for i in permutations(lst, n):
        res.append(''.join(map(str, i)))
    for i in res[::-1]:
        print(i, end = ' ')
    print()