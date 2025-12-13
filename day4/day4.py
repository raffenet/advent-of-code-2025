#!/usr/bin/env python3

import sys
if len(sys.argv) >= 2 and sys.argv[1] == '-s':
    input = open('sample.txt', 'r')
else:
    input = open('input.txt', 'r')

def check(i, j):
    above = grid[i-1] if i > 0 else False
    below = grid[i+1] if i < len(grid)-1 else False
    start = j-1 if j > 1 else 0
    end = j+2 if j < len(grid[0])-1 else j+1
    rolls = 0
    if above:
        rolls = rolls + above[start:end].count('@')
    rolls = rolls + grid[i][start:end].count('@') - 1
    if below:
        rolls = rolls + below[start:end].count('@')

    return rolls < 4

p1 = 0
grid = [list(each.strip()) for each in input.readlines()]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@' and check(i,j):
            p1 = p1 + 1

p2 = 0
p2_old = 0
while True:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@' and check(i,j):
                p2 = p2 + 1
                grid[i][j] = 'x'
    if p2 == p2_old:
        break
    p2_old = p2

print("part 1:", p1)
print("part 2:", p2)
