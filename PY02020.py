n = int(input())
lst = list(map(float, input().split()))
mi = 11
ma = -1
for x in lst:
    mi = min(mi, x)
    ma = max(ma, x)

sum = 0
cnt = 0
for x in lst:
    if x != mi and x != ma:
        sum += x
        cnt += 1
print(f"{sum / cnt:.2f}")
