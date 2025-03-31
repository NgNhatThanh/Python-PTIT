currentId = 1

class KhachHang:
    def __init__(self, id, ten, soCu, soMoi):
        self.id = 'KH' + f'{id:02d}'
        self.ten = ten
        sl = soMoi - soCu
        self.tien = min(sl, 50) * 100
        muc = 1
        if sl > 50:
            muc = 2
            self.tien += (min(sl, 100) - 50) * 150
        if sl > 100:
            muc = 3
            self.tien += (sl - 100) * 200
        if muc == 1:
            self.tien += self.tien * 0.02
        elif muc == 2:
            self.tien += self.tien * 0.03
        else:
            self.tien += self.tien * 0.05


    def __lt__(self, other):
        return self.tien > other.tien

    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + f'{self.tien:.0f}'

n = int(input())
lst = []
for _ in range(n):
    lst.append(KhachHang(currentId, input(), int(input()), int(input())))
    currentId += 1
lst.sort()
for kh in lst:
    print(kh)
