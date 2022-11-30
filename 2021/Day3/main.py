#!/usr/bin/env python3

report = [[c for c in x.strip()] for x in open("input.txt", "r").readlines()]
transpose = ["".join(s) for s in list(zip(*report))]

# Part 1
nums = [num.count("1") >= len(report)/2 for num in transpose]

gamma = int("".join(['1' if i else '0' for i in nums]),2) 
epsilon = gamma ^ 0b111111111111

res_1 = gamma * epsilon

# Part 2

co2_rating = 0
o2_rating = 0

res_2 = co2_rating * o2_rating

print(res_1)
print(res_2)
