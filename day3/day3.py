#!/usr/bin/env python3

import sys
if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    input = open('sample.txt', 'r')
else:
    input = open('input.txt', 'r')

p1 = 0
p2 = 0
batteries = [each.strip() for each in input.readlines()]
for each in batteries:
    first = max(each[:-1])
    second = max(each[each.index(first)+1:])
    p1 = p1 + int(first+second)

    start = 0
    end = -11
    joltage = ""
    while len(joltage) < 12:
        tosearch = each[start:end] if end < 0 else each[start:]
        next = max(tosearch)
        joltage = joltage + next
        start = start + tosearch.index(next) + 1
        end = end + 1
    p2 = p2 + int(joltage)

print("part 1:", p1)
print("part 2:", p2)
