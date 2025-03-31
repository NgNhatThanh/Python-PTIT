from datetime import datetime

currentId = 1

class TramDo:
    def __init__(self, ten, id):
        self.id = 'T' + f'{id:02d}'
        self.ten = ten
        self.thoiGian = 0
        self.luongMua = 0

    def getTrungBinh(self):
        return self.luongMua / (self.thoiGian / 60)

    def boSung(self, thoiGian, luongMua):
        self.thoiGian += thoiGian
        self.luongMua += luongMua

    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + f'{self.getTrungBinh():.2f}'

def chenhLech(batDau, ketThuc):
    return (datetime.strptime(ketThuc, '%H:%M') - datetime.strptime(batDau, '%H:%M')).seconds // 60

n = int(input())
mp = {}
for _ in range(n):
    ten = input()
    batDau = input()
    ketThuc = input()
    luongMua = int(input())
    if mp.get(ten, 0) == 0:
        td = TramDo(ten, currentId)
        currentId += 1
        td.boSung(chenhLech(batDau, ketThuc), luongMua)
        mp[td.ten] = td
    else:
        mp[ten].boSung(chenhLech(batDau, ketThuc), luongMua)

for x in mp.values():
    print(x)
