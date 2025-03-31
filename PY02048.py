n, k = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst.sort()
res = 1
for i in range(n - 1):
    if(lst[i + 1] - lst[i] > k):
        res += 1
print(res)