from datetime import datetime

currentId = 1

class KhachHang:
    def __init__(self, id, ten, soPhong, ngayNhan, ngayTra, tienPhatSinh):
        self.id = f'KH{id:02d}'
        self.ten = ten
        self.soPhong = soPhong
        self.ngayNhan = ngayNhan
        self.ngayTra = ngayTra
        self.tienPhatSinh = tienPhatSinh

    def getTang(self):
        return int(self.soPhong[0])

    def getTongTien(self):
        tien = 0
        tang = self.getTang()
        if tang == 1:
            tien = 25
        elif tang == 2:
            tien = 34
        elif tang == 3:
            tien = 50
        elif tang == 4:
            tien = 80
        return tien * self.getSoNgayO() + int(self.tienPhatSinh)

    def getSoNgayO(self):
        return (datetime.strptime(self.ngayTra, '%d/%m/%Y')
                - datetime.strptime(self.ngayNhan, '%d/%m/%Y')).days + 1

    def __str__(self):
        return ' '.join([self.id, self.ten, str(self.soPhong), str(self.getSoNgayO()), str(self.getTongTien())])

n = int(input())
lst = []
for i in range(n):
    kh = KhachHang(currentId, input().strip(), input().strip(), input().strip(), input().strip(), input().strip())
    lst.append(kh)
    currentId += 1
lst.sort(key = lambda x: -x.getTongTien())
for kh in lst:
    print(kh)