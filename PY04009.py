class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def __add__(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)

    def __mul__(self, other):
        return SoPhuc(self.thuc * other.thuc - self.ao * other.ao, self.thuc * other.ao + self.ao * other.thuc)

    def __str__(self):
        s = str(self.thuc)
        if self.ao < 0:
            s += ' - ' + str(self.ao * -1) + 'i'
        else:
            s += ' + ' + str(self.ao) + 'i'
        return s

t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    sp1 = SoPhuc(int(a[0]), int(a[1]))
    sp2 = SoPhuc(int(a[2]), int(a[3]))
    sp3 = (sp1 + sp2) * sp1
    sp4 = (sp1 + sp2) * (sp1 + sp2)
    print(sp3, sp4, sep = ', ')