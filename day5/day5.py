#!/usr/bin/env python3

import re

def read_input_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def calculate_id(seat):
    return int(seat.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)

lines = read_input_file('day5_1.txt')
seats = sorted([calculate_id(seat) for seat in lines])

max = 0
for s in seats:
    if s > max:
        max = s
print(max)

for i in range(0, 1024):
    if i not in seats:
        print(i)
