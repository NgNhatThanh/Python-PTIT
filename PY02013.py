while True:
    n = int(input())
    if n == 0:
        break
    b = {}
    lst = [n]
    b[n] = 1
    while b.get(1, 0) == 0:
        tmp = lst[0]
        lst.pop(0)
        if tmp % 2 == 0 and b.get(tmp // 2, 0) == 0:
            b[tmp // 2] = 1
            lst.append(tmp // 2)
        if tmp % 2 == 1 and b.get(tmp * 3 + 1, 0) == 0:
            b[tmp * 3 + 1] = 1
            lst.append(tmp * 3 + 1)
    print(len(b))
