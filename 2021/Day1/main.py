#!/usr/bin/env python3

depths = [int(x) for x in open("input.txt", "r").readlines()]

# Part 1
res_1 = sum([depths[x] > depths[x-1] for x in range(1,len(depths))])

# Part 2
depths = [(depths[x] + depths[x+1] + depths[x+2]) for x in range(len(depths) - 2)]
res_2 = sum([depths[x] > depths[x-1] for x in range(1,len(depths))])

print(res_1)
print(res_2)
