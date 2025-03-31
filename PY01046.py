def thapHaNoi(src, mid, des, n):
    if n == 1:
        print(str(src) + " -> " + str(des))
        return
    thapHaNoi(src, des, mid, n - 1)
    thapHaNoi(src, mid, des, 1)
    thapHaNoi(mid, src, des, n - 1)

n = int(input())
thapHaNoi('A', 'B', 'C', n)
