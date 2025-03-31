class SinhVien:
    def __init__(self, ten, lamDung, submit):
        self.ten = ten
        self.lamDung = lamDung
        self.submit = submit

    def __lt__(self, other):
        if self.lamDung == other.lamDung:
            if self.submit == other.submit:
                return self.ten < other.ten
            return self.submit < other.submit
        return self.lamDung > other.lamDung

    def __str__(self):
        return self.ten + ' ' + str(self.lamDung) + ' ' + str(self.submit)


n = int(input())
lst = []
for _ in range(n):
    ten = input()
    ld, sub = list(map(int, input().split()))
    sv = SinhVien(ten, ld, sub)
    lst.append(sv)
lst.sort()
for sv in lst:
    print(sv)

