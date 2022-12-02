#!/usr/bin/env python3

cals = [x.split("\n") for x in open("input.txt", "r").read().strip().split("\n\n")]
cals = [sum(int(y) for y in x) for x in cals]
cals.sort(reverse=True)

res_1 = cals[0]
res_2 = sum(cals[0:3])

print(res_1)
print(res_2)
