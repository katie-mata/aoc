#!/usr/bin/env python3

from itertools import accumulate, cycle

def parse_input():
    with open('day1_1.txt', 'r') as f:
        return [int(l.strip()) for l in f.readlines()]

def part_a(changes):
    return sum(changes)

def part_b(changes):
    seen = set()
    iterable = accumulate(cycle(changes))
    for i in iterable:
        if i in seen:
            return(i)
        seen.add(i)

changes = parse_input()

print(part_a(changes))
print(part_b(changes))
