#!/usr/bin/env python3

answers = open("input.txt", "r").read().split("\n\n")

# Part 1
res_1 = sum([len(set(answer.replace("\n", ""))) for answer in answers])

# Part 2
res_2 = 0

for answer in answers:
    answer = [set(x) for x in answer.strip().split("\n")]
    s1 = answer[0]
    
    for s in answer[1:]:
        s1 = s1.intersection(s)
    
    res_2 = res_2 + len(s1)

print(res_1)
print(res_2)
