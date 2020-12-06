#!/usr/bin/env python3

def read_input_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines() # removes '/n'

lines = read_input_file('day6_1.txt')
print(lines)
