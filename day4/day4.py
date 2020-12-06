#!/usr/bin/env python3

import re

def read_input_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def process_input(input):
    return [entry.strip().replace('\n', ' ') for entry in input.split('\n\n')]

def generate_key_pattern(key):
    return re.compile('.*' + key + ':(\S+)')

# key validation
byr_key_pattern = generate_key_pattern('byr')
iyr_key_pattern = generate_key_pattern('iyr')
eyr_key_pattern = generate_key_pattern('eyr')
hgt_key_pattern = generate_key_pattern('hgt')
hcl_key_pattern = generate_key_pattern('hcl')
ecl_key_pattern = generate_key_pattern('ecl')
pid_key_pattern = generate_key_pattern('pid')

def validate_key(pattern, key):
    return pattern.match(key)

def key_dispatcher(key, value):
    return {
        'byr': validate_key(byr_key_pattern, value),
        'iyr': validate_key(iyr_key_pattern, value),
        'eyr': validate_key(eyr_key_pattern, value),
        'hgt': validate_key(hgt_key_pattern, value),
        'hcl': validate_key(hcl_key_pattern, value),
        'ecl': validate_key(ecl_key_pattern, value),
        'pid': validate_key(pid_key_pattern, value),
    }[key]

# value validation
year_value_pattern = re.compile('^\d{4}$')
hgt_cm_value_pattern = re.compile('^(\d+)cm$')
hgt_in_value_pattern = re.compile('^(\d+)in$')
hcl_value_pattern = re.compile('^#[0-9a-f]{6}$')
pid_value_pattern = re.compile('^\d{9}$')

def validate_year(value, min, max):
    return bool(year_value_pattern.search(value) and int(value) >= min and int(value) <= max)

def byr(value):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    return validate_year(value, 1920, 2002)

def iyr(value):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    return validate_year(value, 2010, 2020)

def eyr(value):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    return validate_year(value, 2020, 2030)

def hgt(value):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    m = hgt_cm_value_pattern.match(value)
    if m is not None:
        height = int(m.group(1))
        return height >= 150 and height <= 193

    m = hgt_in_value_pattern.match(value)
    if m is not None:
        height = int(m.group(1))
        return height >= 59 and height <= 76

    return False

def hcl(value):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    return bool(hcl_value_pattern.search(value))

def ecl(value):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid(value):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    return bool(pid_value_pattern.search(value))

value_dispatch_table = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid
}

def validate(entry, keys_only=False):
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for key in required_keys:
        m = key_dispatcher(key, entry)
        if m is None:
            return False
        if keys_only is True:
            continue
        if value_dispatch_table[key](m.group(1)) is False:
            return False
    return True

entries = process_input(read_input_file('day4_1.txt'))

valid_entries = [entry for entry in entries if validate(entry, keys_only=True)]
print(len(valid_entries))

valid_entries = [entry for entry in entries if validate(entry)]
print(len(valid_entries))
