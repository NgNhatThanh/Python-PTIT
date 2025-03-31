import math


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def toiGian(self):
        g = math.gcd(self.tu, self.mau)
        self.tu //= g
        self.mau //= g

    def __str__(self):
        return str(self.tu) +  '/' + str(self.mau)

tu, mau = list(map(int, input().split()))
ps = PhanSo(tu, mau)
ps.toiGian()
print(ps)