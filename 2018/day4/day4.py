#!/usr/bin/env python3

import collections
import re

def parse_input():
    with open('./day4_1.txt', 'r') as f:
        lines = f.read().splitlines()

    guards = collections.defaultdict(list)
    times = collections.defaultdict(int)

    for line in sorted(lines):
        m = re.search('Guard #(\d+)', line)
        if m is not None:
            guard = int(m.group(1))

        m = re.search(':(\d+)\] falls asleep', line)
        if m is not None:
            start = int(m.group(1))

        m = re.search(':(\d+)\] wakes up', line)
        if m is not None:
            end = int(m.group(1))
            guards[guard].append((start, end))
            times[guard] += end - start
         
    return guards, times

def part_a(guards, times):
    guard, time = max(times.items(), key=lambda i: i[1])
    minute, count = max([ (minute, sum(1 for start, end in guards[guard] if start <= minute < end)) for minute in range(60)], key=lambda i: i[1])

    return guard * minute

def part_b(guards, times):
    guard, minute, count = max([ (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end)) for minute in range(60) for guard in guards], key=lambda i: i[2])

    return guard * minute

guards, times = parse_input()
print(part_a(guards, times))
print(part_b(guards, times))
