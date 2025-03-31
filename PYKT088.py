import math

n = int(input())
nt = []

def check(n):
    can = int(math.sqrt(n)) + 1
    for i in range(2, can):
        if n % i == 0:
            return False
    return True

for i in range(2, int(math.sqrt(n)) + 1):
    if check(i):
        nt.append(i)

res = 0
for i in range(len(nt)):
    if nt[i] ** 8 <= n:
        res += 1
    if i < len(nt) - 1 and (nt[i] ** 2) * (nt[i + 1] ** 2) >= n:
        break
    for j in range(i + 1, len(nt)):
        if (nt[i] ** 2) * (nt[j] ** 2) <= n:
            res += 1

print(res)



