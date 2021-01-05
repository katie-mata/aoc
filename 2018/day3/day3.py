#!/usr/bin/env python3

import re
from collections import Counter

def parse_input():
    with open('./day3_1.txt', 'r') as f:
        lines = f.readlines()
        claims = {}
        for line in lines:
            m = re.match('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
            id = m.group(1)
            start_x, start_y, width, length = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
            claims[id] = [(x, y) for x in range(start_x, start_x + width) for y in range(start_y, start_y + length)]

        return claims

def make_counter(claims):
    counter = Counter()
    for claim in claims.values():
        for point in claim:
            counter.update([point])

    return counter

def part_a(claims):
    counter = make_counter(claims)
    return sum([1 for tuple, count in counter.items() if count > 1])

def is_intact(claim, counter):
    for point in claim:
        if counter[point] != 1:
            return False

    return True

def part_b(claims):
    counter = make_counter(claims)
    for id, claim in claims.items():
        if is_intact(claim, counter):
            return id

claims = parse_input()
print(part_a(claims))
print(part_b(claims))
