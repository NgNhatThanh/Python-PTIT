with open('CONTACT.in', 'r') as f:
    lst = list(set(x.lower() for x in f.read().splitlines()))
    lst.sort()
    for s in lst:
        print(s)

