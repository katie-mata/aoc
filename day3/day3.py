#!/usr/bin/env python3

import re

def read_input_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def create_map(lines):
    map = {}

    for line_num, line in enumerate(lines):
        for char_num, char in enumerate(line):
            map[(char_num, line_num)] = char == '#'

    return map

def create_path(right, down, max_x, max_y, map):
    current_x, current_y, num_trees = 0, 0, 0

    while True:
        if current_y >= max_y:
            break
        num_trees += map[(current_x%max_x, current_y)]
        current_x += right
        current_y += down

    return num_trees

lines = read_input_file('./day3_1.txt')
map = create_map(lines)

count1 = create_path(3, 1, len(lines[0]), len(lines), map)
count2 = create_path(1, 1, len(lines[0]), len(lines), map)
count3 = create_path(5, 1, len(lines[0]), len(lines), map)
count4 = create_path(7, 1, len(lines[0]), len(lines), map)
count5 = create_path(1, 2, len(lines[0]), len(lines), map)

print(count1)
print(count1 * count2 * count3 * count4 * count5)
