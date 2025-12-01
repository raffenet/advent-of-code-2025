#!/usr/bin/env python3

import sys
if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    input = open('sample.txt', 'r')
else:
    input = open('input.txt', 'r')

pairs = [(each[0],int(each[1:].strip())) for each in input.readlines()]
pos = 50
p1 = 0
p2 = 0
for each in pairs:
    start = pos
    p2 = p2 + int(each[1]/100)
    move = each[1] % 100

    if each[0] == 'L':
        pos = pos - move
    else:
        pos = pos + move

    if pos == 100:
        pos = 0

    if pos > 100:
        pos = pos - 100
        if start != 0:
            p2 = p2 + 1
    elif pos < 0:
        pos = pos + 100
        if start != 0:
            p2 = p2 + 1

    if pos == 0:
        p1 = p1 + 1
        p2 = p2 + 1

print("part 1:", p1)
print("part 2:", p2)
