currentId = 1

class HocSinh:
    def __init__(self, ten, dsDiem, id):
        self.id = 'HS' + f'{id:02d}'
        self.ten = ten
        self.dsDiem = dsDiem
        tb = (dsDiem[0] + dsDiem[1]) * 2
        for i in range(2, len(dsDiem)):
            tb += dsDiem[i]
        tb = tb / 10 / 1.2
        self.diemTb = tb
        if tb >= 9:
            self.xepLoai = 'XUAT SAC'
        elif tb >= 8:
            self.xepLoai = 'GIOI'
        elif tb >= 7:
            self.xepLoai = 'KHA'
        elif tb >= 5:
            self.xepLoai = 'TB'
        else:
            self.xepLoai = 'YEU'

    def __lt__(self, other):
        if self.diemTb == other.diemTb:
            return self.id < other.id
        return self.diemTb > other.diemTb

    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + f'{self.diemTb:.1f}' + ' ' + self.xepLoai

n = int(input())
lst = []
for _ in range(n):
    lst.append(HocSinh(input(), list(map(float, input().split())), currentId))
    currentId += 1
lst.sort()
for hs in lst:
    print(hs)