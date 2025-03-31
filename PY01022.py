n = input()
if len(n) == 1:
    print(1)
else:
    res = 0
    while len(n) != 1:
        sum = 0
        for c in n:
            sum += ord(c) - ord('0')
        n = str(sum)
        res += 1
    print(res)
