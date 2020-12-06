#!/usr/bin/env python3

import re

def read_input_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def valid1(min, max, char, pwd):
    count = pwd.count(char)
    return count >= min and count <= max

def valid2(min, max, char, pwd):
    char_in_min = pwd[min-1] == char
    char_in_max = pwd[max-1] == char
    return char_in_min != char_in_max        

pattern = re.compile('(\d+)-(\d+) (\w): (\w+)')

def parse(data, validation):
    m = pattern.match(data)
    min = int(m.group(1))
    max = int(m.group(2))
    char = m.group(3)
    pwd = m.group(4)

    return validation(min, max, char, pwd)
  
lines = read_input_file('./day2_1.txt')
print(sum([1 for line in lines if parse(line, valid1)]))
print(sum([1 for line in lines if parse(line, valid2)]))
