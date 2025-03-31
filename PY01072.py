n, k = list(map(int, input().split()))
lst = sorted(list(set(list(map(int, input().split())))))

idx = [0] * (k + 1)

def Try(i):
    if i == k + 1:
        for j in range(1, k + 1):
            print(lst[idx[j] - 1], end = ' ')
        print()
        return
    for j in range(idx[i - 1] + 1, len(lst) + 1):
        idx[i] = j
        Try(i + 1)

Try(1)


