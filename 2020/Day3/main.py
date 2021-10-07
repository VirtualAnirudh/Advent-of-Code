#!/usr/bin/env python3

grid = open("input.txt", "r")
grid = [x.strip() for x in grid.readlines()]

row_len = len(grid[0])
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

res_1 = []
res_2 = 1

for (x,y) in slopes:
    i = 0
    trees = 0

    for row in grid[::y]:
        if row[i] == "#":
            trees = trees + 1
        i = (i + x) % row_len
    
    res_1.append(trees)
    res_2 = res_2 * trees

print(res_1)
print(res_2)
