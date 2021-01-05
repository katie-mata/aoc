#!/usr/bin/env python3

from string import ascii_uppercase, ascii_lowercase

def read_input():
    with open('./day5_1.txt', 'r') as f:
        return f.read().strip()

def part_a(input, ignore=[]):
    i = 0

    buffer = []
    for c in input:
        if c in ignore:
            continue
 
        if buffer and c == buffer[-1].swapcase(): 
            buffer.pop()
        else:
            buffer.append(c)

    return len(buffer)

def part_b(input):
    return min((part_a(input, unit) for unit in zip(ascii_uppercase, ascii_lowercase)))

input = read_input()
print(part_a(input))
print(part_b(input))
