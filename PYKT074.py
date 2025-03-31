t = int(input())
for _ in range(t):
    ws = input().split()
    lenght = 0
    for w in ws:
        lenght += len(w)
        if lenght > 100:
            break
        print(w, end = ' ')
        lenght += 1
    print()