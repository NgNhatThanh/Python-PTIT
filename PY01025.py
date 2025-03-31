n = input()
res = []
for i, digit in enumerate(reversed(n)):
    if i % 3 == 0 and i != 0:
        res.append(',')
    res.append(digit)
print(''.join(reversed(res)))

