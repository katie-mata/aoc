#!/usr/bin/env python3

import itertools
import operator
from functools import reduce

def read_input_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def parse_input(input):
    return list(map(int, input))

def find_tuples(numbers, tuple_len):
    combinations = itertools.combinations(numbers, tuple_len)
    return [c for c in list(combinations) if sum(c) == 2020]

def get_product(numbers):
    return reduce(operator.mul, numbers, 1)

pairs = find_tuples(parse_input(read_input_file('day1_1.txt')), 2)
print(get_product(pairs[0]))

triples = find_tuples(parse_input(read_input_file('day1_1.txt')), 3)
print(get_product(triples[0]))
