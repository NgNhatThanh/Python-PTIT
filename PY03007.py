import re
from sys import stdin

s = ''

inp = stdin.read()
for ss in inp.splitlines():
    s += ss + ' '

sentences = re.split('[.?!]+', s)

for sentence in sentences:
    sentence = sentence.lower()
    ws = sentence.split()
    if len(ws) > 0:
        ws[0] = ws[0].capitalize()
    for w in ws:
        print(w, end = ' ')
    print()


