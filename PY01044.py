s1 = input().lower()
s2 = input().lower()
se1 = set(s1.split())
se2 = set(s2.split())
hop = se1.union(se2)
giao = se1.intersection(se2)
l1 = list(hop)
l2 = list(giao)
l1.sort()
l2.sort()
print(' '.join(l1))
print(' '.join(l2))