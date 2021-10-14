#!/usr/bin/env python3

import re

data = open("input.txt", "r").read()
data = data.split("\n\n")

keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
patterns = [r"byr:19[2-9][0-9]|200[0-2]\b",
            r"iyr:201[0-9]|2020\b",
            r"eyr:202[0-9]|2030\b",
            r"hgt:1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
            r"hcl:#[0-9a-f]{6}\b",
            r"ecl:amb|blu|brn|gry|grn|hzl|oth\b",
            r"pid:[0-9]{9}\b"]

res_1 = 0
res_2 = 0

for passport in data:
    if all([key in passport for key in keys]):
        res_1 = res_1 + 1

        if all([re.search(pattern, passport) for pattern in patterns]):
            res_2 = res_2 + 1
    

print(res_1)
print(res_2)


