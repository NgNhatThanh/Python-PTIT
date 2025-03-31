with open('DATA.in', 'r') as f:
    t = int(f.readline())
    for _ in range(t):
        b = int(f.readline())
        s = f.readline().strip()
        tp = 0
        for i in range(len(s) - 1, -1, -1):
            tp += (1 << (len(s) - 1 - i)) * (ord(s[i]) - ord('0'))
        res = ''
        while tp > 0:
            c = tp % b
            if c >= 10:
                c = chr(ord('A') + c - 10)
            res += str(c)
            tp //= b
        res = res[::-1]
        print(res)
