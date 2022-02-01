from collections import Counter, defaultdict
import numpy as np
from pprint import pprint
from itertools import permutations
import re

day = "04"
exercise_file = r"..\data\d{0}.txt".format(day)
example_file = r"..\data\d{0}eg.txt".format(day)

expected_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
eyes_colours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def create_passport(fields):
    passport = {}
    for f in fields:
        name, value = f.split(':')
        passport[name] = value
    return passport

def get_input(input_file):
    passports = []
    fields = []
    for x in open(input_file):
        if x == '\n':
            passports.append(create_passport(fields))
            fields = []
        else:
            fields.extend(x.strip('\n').split(' '))
    if fields:
        passports.append(create_passport(fields))
    return passports

def additional_criteria(p):
    assert 1920 <= int(p['byr']) <= 2002
    assert 2010 <= int(p['iyr']) <= 2020
    assert 2020 <= int(p['eyr']) <= 2030

    h_unit = p['hgt'][-2:]
    h_value = int(p['hgt'][:-2])
    if h_unit == "cm":
        assert 150 <= h_value <= 193
    elif h_unit == "in":
        assert 59 <= h_value <= 76
    else:
        raise Exception("invalid h_unit")

    assert p['hcl'][:1] == '#'
    hair_colour = p['hcl'][1:]
    assert len(hair_colour) == 6
    result = re.search('[^a-f0-9]', hair_colour, re.I)
    assert result is None

    assert p['ecl'] in eyes_colours

    assert len(p['pid']) == 9
    assert p['pid'].isnumeric()

def is_passport_valid(passport, use_p2_criteria):
    diff = expected_fields.difference(set(passport.keys()))
    diff.discard('cid')
    try:
        assert len(diff) == 0
        if use_p2_criteria:
            additional_criteria(passport)
    except Exception as e:
        return False
    return True

def solution(input, part2):
    valid = 0
    for passport in input:
        if is_passport_valid(passport, part2):
            valid += 1
    return valid

example_input = get_input(example_file)
exercise_input = get_input(exercise_file)

print(solution(example_input, False)) #2
print(solution(exercise_input, False)) #196 #35
print(solution(exercise_input, True)) #114 #60