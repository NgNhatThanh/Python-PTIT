import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def toiGian(self):
        g = math.gcd(self.tu, self.mau)
        self.tu //= g
        self.mau //= g

    def add(self, other):
        t = self.tu * other.mau + self.mau * other.tu
        m = self.mau * other.mau
        return PhanSo(t, m)

    def __str__(self):
        return str(self.tu) +  '/' + str(self.mau)

t1, m1, t2, m2 = list(map(int, input().split()))
p1 = PhanSo(t1, m1)
p2 = PhanSo(t2, m2)
p3 = p1.add(p2)
p3.toiGian()
print(p3)