#!/usr/bin/env python3

def score(x, y):
    if(x == y):
        return 3 + y
    elif(y == x % 3 + 1):
        return 6 + y
    return y

def score_2(x, y):
    if(y == 3):
        return 6 + (x % 3 + 1)
    elif(y == 2):
        return 3 + x
    else:
        return 0 + ((x + 1) % 3 + 1)

data = open("input.txt", "r")
data = [x.replace("A", "1")
                    .replace("B", "2")
                    .replace("C", "3")
                    .replace("X", "1")
                    .replace("Y", "2")
                    .replace("Z", "3")
                    .split(" ") for x in data.read().strip().split("\n")]

res_1 = sum([score(int(x[0]), int(x[1])) for x in data])
res_2 = sum([score_2(int(x[0]), int(x[1])) for x in data])

print(res_1)
print(res_2)

