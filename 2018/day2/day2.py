#!/usr/bin/env python3

from collections import Counter
from itertools import combinations, compress

def read_input():
    with open('./day2_1.txt', 'r') as f:
        return f.read().splitlines()

def part_a(input):        
    input = [Counter(i) for i in input]
    twos, threes = 0, 0
    for i in input:
        counts = i.values()
        if 2 in counts:
            twos += 1
        if 3 in counts:
            threes += 1

    return twos * threes

def part_b(input):
    for first, second in combinations(input, 2):
        difference = [e1 == e2 for e1, e2 in zip(first, second)]
        if sum(difference) == (len(first) - 1):
            return ''.join(list(compress(first, difference)))

input = read_input()
print(part_a(input))
print(part_b(input))
