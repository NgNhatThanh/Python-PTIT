class ThiSinh:
    def __init__(self, ten, ngaySinh, d1: float, d2: float, d3: float):
        self.ten = ten
        self.ngaySinh = ngaySinh
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.tongDiem = d1 + d2 + d3

    def __str__(self):
        return self.ten + ' ' + self.ngaySinh + ' ' + f'{self.tongDiem:.1f}'

ten = input()
ngaySinh = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())
ts = ThiSinh(ten, ngaySinh, d1, d2, d3)
print(ts)