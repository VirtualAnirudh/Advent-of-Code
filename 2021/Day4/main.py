#!/usr/bin/env python3

data = open("input.txt", "r").read().split("\n\n")

draw = data[0].split(",")
boards = [x.split("\n") for x in data[1:]]

