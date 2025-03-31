t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    mp1 = {}
    mp2 = {}
    mp3 = {}
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    for x in a:
        mp1[x] = mp1.get(x, 0) + 1
    for x in b:
        mp2[x] = mp2.get(x, 0) + 1
    for x in c:
        mp3[x] = mp3.get(x, 0) + 1
    se1 = set(a)
    se2 = set(b).intersection(se1)
    se3 = sorted(set(c).intersection(se2))
    if len(se3) == 0:
        print("NO")
    else:
        for x in se3:
            for i in range(min(mp1[x], mp2[x], mp3[x])):
                print(x, end=' ')
        print()

