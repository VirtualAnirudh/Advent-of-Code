#!/usr/bin/env python3

years = open("input.txt", "r")
years = years.read().strip().split("\n")
years = [int(x) for x in years]

years = sorted(years)

# Part 1
for x in years:
    y = (2020 - x) 
    if y in years:
        print(x, y)
        print(x * y)
        break

# Part 2
for x in years:
    for y in years: 
        z = (2020 - x - y) 
        if z in years:
            print(x, y, z)
            print(x * y * z)
            exit(0)

        
