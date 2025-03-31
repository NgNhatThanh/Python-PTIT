tem = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    lst = input().split()
    if len(lst) == 1:
        break
    k = int(lst[0])
    s = list(lst[1])
    res = ""
    for x in s:
        idx = tem.find(x)
        res += tem[(idx + k) % 28]
    res = res[::-1]
    print(res)
