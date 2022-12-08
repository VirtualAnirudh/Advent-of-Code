#!/usr/bin/env python3

def chartonum(c):
    if(c.isupper()):
        return ord(c) - 65 + 27
    elif(c.islower()):
        return ord(c) - 97 + 1

data = open("input.txt", "r").read().strip().split("\n")

res_1 = sum([chartonum("".join(str(i) for i in set(x[0:len(x)//2]) & set(x[len(x)//2:]))) 
                                    for x in data])
res_2 = sum([chartonum("".join(str(i) for i in set(data[x]) & set(data[x+1]) & set(data[x+2]))) 
                                    for x in range(0, len(data), 3)])

print(res_1)
print(res_2)
