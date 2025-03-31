class SinhVien:
    def __init__(self, msv, ten, lop):
        self.msv = msv
        self.ten = ten
        self.lop = lop

    def setDiemChuyenCan(self, chuyenCan: str):
        cc = 10
        for i in range(len(chuyenCan)):
            if chuyenCan[i] == 'm':
                cc -= 1
            elif chuyenCan[i] == 'v':
                cc -= 2
        if cc < 0:
            cc = 0
        self.diemChuyenCan = cc

    def __str__(self):
        res = ' '.join([self.msv, self.ten, self.lop, str(self.diemChuyenCan)])
        if self.diemChuyenCan == 0:
            res += ' KDDK'
        return res

n = int(input())
lst = []
mp = {}
for i in range(n):
    sv = SinhVien(input(), input(), input())
    lst.append(sv)
    mp[sv.msv] = sv
for i in range(n):
    msv, cc = input().split()
    mp[msv].setDiemChuyenCan(cc)
for sv in lst:
    print(sv)