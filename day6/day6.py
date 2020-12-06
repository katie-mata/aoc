#!/usr/bin/env python3

from functools import reduce

def read_input_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip()

def create_sets(input):
    return [{char for form in group.split('\n') for char in form} for group in input.split('\n\n')]

def create_intersections(input):
    intersections = []
    for group in input.split('\n\n'):
        sets = [{char for char in form} for form in group.split('\n')]
        head, *tail = sets
        intersections.append(head.intersection(*tail))

    return intersections

input = read_input_file('day6_1.txt')
sets = create_sets(input)
print(sum([len(set) for set in sets]))

intersections = create_intersections(input)
print(sum([len(intersection) for intersection in intersections]))
