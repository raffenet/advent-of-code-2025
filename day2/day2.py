#!/usr/bin/env python3

import sys
if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    input = open('sample.txt', 'r')
else:
    input = open('input.txt', 'r')

p1 = 0
p2 = 0
ranges = [tuple(each.split('-')) for each in input.readline().strip().split(',')]
for each in ranges:
    for id in range(int(each[0]), int(each[1]) + 1):
        import re
        strid = str(id)
        half = len(strid) // 2
        if strid[:half] == strid[half:]:
            p1 = p1 + id
        for n in range(1, half+1):
            if re.match(f"^({strid[:n]})+$", strid[n:]):
                p2 = p2 + id
                break

print("part 1:", p1)
print("part 2:", p2)
