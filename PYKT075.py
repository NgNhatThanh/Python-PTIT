class LienLac:
    def __init__(self, ten, sdt, ngay):
        self.ten = ten
        self.sdt = sdt
        self.ngay = ngay

    def __lt__(self, other):
        ws1 = self.ten.split()
        ws2 = self.ten.split()
        if ws1[len(ws1) - 1] == ws2[len(ws2) - 1]:
            hd1 = ' '.join(ws1[:len(ws1) - 1])
            hd2 = ' '.join(ws2[:len(ws2) - 1])
            return hd1 < hd2
        return ws1[len(ws1) - 1] < ws2[len(ws2) - 1]

    def __str__(self):
        return self.ten + ': ' + self.sdt + ' ' + self.ngay

lst = []

with open('SOTAY.txt', 'r') as f1:
    ds = f1.read().splitlines()
    i = 0
    while i < len(ds):
        ngay = ds[i].split()[1]
        i += 1
        while True:
            lst.append(LienLac(ds[i], ds[i + 1], ngay))
            i += 2
            if i >= len(ds) or ds[i][7] == '/':
                break
    f1.close()

lst.sort()
with open('DIENTHOAI.txt', 'w') as f2:
    for ll in lst:
        f2.write(str(ll) + '\n')
    f2.close()

