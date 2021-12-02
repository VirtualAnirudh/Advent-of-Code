#!/usr/bin/env python3

commands = [x.strip().split(" ") for x in open("input.txt", "r").readlines()]

x_pos = 0
y_pos = 0

aim = 0
depth = 0

for pos,num in commands:
    num = int(num)
    if pos == "forward":
        x_pos += num
        depth += aim * num

    if pos == "down":
        y_pos += num
        aim += num
    elif pos == "up":
        y_pos -= num
        aim -= num

res_1 = x_pos * y_pos
res_2 = x_pos * depth

print(res_1)
print(res_2)
