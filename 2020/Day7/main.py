#!/usr/bin/env python3

import re

class tree:
    def __init__(self, name = "root", children = None):
        

rules = [rule.strip() for rule in open("input.txt", "r").readlines()]

rules = [rule.split(" contain ") for rule in rules]
bags = {rule[0]: rule[1] for rule in rules}

for key, value in bags.items():
    print(key + ": " + value)

res_1 = []
res_2 = 0

