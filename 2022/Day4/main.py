#!/usr/bin/env python3

def overlap(x, y, full):
    x1,x2 = map(int,x.split("-"))
    y1,y2 = map(int,y.split("-"))
    
    if full:
        if((x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2)):
            return 1
        else:   
            return 0
    else:
        if((x1 <= y1 and x2 >= y1) or (x1 <= y2 and x2 >= y2) or (y1 <= x1 and y2 >= x1) or (y2 <= x1 and y2 >= x2)):
            return 1
        else:   
            return 0


sect = [x.split(",") for x in open("input.txt", "r").read().strip().split("\n")]

res_1 = sum([overlap(x[0], x[1], True) for x in sect])
res_2 = sum([overlap(x[0], x[1], False) for x in sect])

print(res_1)
print(res_2)
