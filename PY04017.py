class TayDua:
    def __init__(self, ten, donVi, denDich):
        self.ten = ten
        self.donVi = donVi
        lst = donVi.split() + ten.split()
        self.id = ''
        for w in lst:
            self.id += w[0].upper()
        self.vanToc = 120 / float(int(denDich[:1]) - 6 + float(int(denDich[2:]) / 60))

    def __lt__(self, other):
        return self.vanToc < other.vanToc

    def __str__(self):
        return ' '.join([self.id, self.ten, self.donVi, f'{round(self.vanToc)}', 'Km/h'])

n = int(input())
lst = []
for i in range(n):
    lst.append(TayDua(input(), input(), input()))
lst.sort(reverse=True)
for td in lst:
    print(td)