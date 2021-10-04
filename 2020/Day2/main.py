#!/usr/bin/env python3

import re
from operator import xor

passwords = open("input.txt", "r")
passwords = passwords.read().strip().split("\n")

res_1 = 0
res_2 = 0

for password in passwords:
    # Format -> 2-5 s: password
    pattern = r"^([0-9]+)-([0-9]+) (\w): ([\w]+)$"
    res = re.search(pattern, password)
    
    if res is not None:
        lower = int(res[1])
        upper = int(res[2])
        letter = res[3]
        passwd = res[4]
    
        # Part 1
        occurances = len(re.findall(letter, passwd))

        if (occurances >= lower) and (occurances <= upper):
            res_1 += 1
        
        # Part 2
        if xor(passwd[lower-1] == letter, passwd[upper-1] == letter):
            res_2 += 1

print(res_1)
print(res_2)
