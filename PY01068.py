from itertools import combinations

n, k = list(map(int, input().split()))
se = sorted(set(input().split()))
for s in combinations(se, k):
    print(*s)