from datetime import datetime

currentId = 1

class CaThi:
    def __init__(self, id, ngayThi, gioThi, phongThi):
        self.id = f'C{id:03d}'
        self.ngayThi = ngayThi
        self.gioThi = gioThi
        self.phongThi = phongThi

    def __lt__(self, other):
        if self.ngayThi == other.ngayThi:
            if self.gioThi == other.gioThi:
                return self.id < other.id
            return self.gioThi < other.gioThi
        return datetime.strptime(self.ngayThi, '%d/%m/%Y') < datetime.strptime(other.ngayThi, '%d/%m/%Y')

    def __str__(self):
        return ' '.join([self.id, str(self.ngayThi), str(self.gioThi), self.phongThi])

with open('CATHI.in', 'r') as f:
    n = int(f.readline())
    lst = []
    for i in range(n):
        lst.append(CaThi(currentId, f.readline().strip(), f.readline().strip(), f.readline().strip()))
        currentId += 1
    lst.sort()
    for ct in lst:
        print(ct)