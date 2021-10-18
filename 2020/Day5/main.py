#!/usr/bin/env python3

seats = open("input.txt", "r")
seats = [x.strip().replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1") for x in seats.readlines()]

seat_ids = []

for seat in seats:
    seat_num = (int(seat[0:7], 2) * 8) + int(seat[7:], 2)
    seat_ids.append(seat_num)

seat_ids.sort()

# Part 1
res_1 = seat_ids[-1]

# Part 2

ap_sum = (len(seat_ids) + 1) * ((seat_ids[0] + seat_ids[-1]) / 2) # Sum of AP -> number of terms * (first term + last term)/2
res_2 = int(ap_sum - sum(seat_ids))

print(res_1)
print(res_2)
