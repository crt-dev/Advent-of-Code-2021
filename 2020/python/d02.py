from collections import Counter, defaultdict
import numpy as np
from pprint import pprint
from itertools import permutations

day = "02"
exercise_file = r"..\data\d{0}.txt".format(day)
example_file = r"..\data\d{0}eg.txt".format(day)

def get_input(input_file):
    input = [x.strip() for x in open(input_file)]
    return input

def is_valid(input, part2):
    s = input.split(":")
    password = s[1].strip()
    letter = s[0][-1]
    range = s[0][0:-2].split("-")
    r = int(range[0]), int(range[1])

    counter = Counter(password)
    count = counter.get(letter)
    if count is None:
        count = 0
    if part2:
        r = r[0] - 1, r[1] - 1
        if r[0] > len(password) or r[1] > len(password):
            return False
        else:
            return (password[r[0]] == letter) != (password[r[1]] == letter)
    else:
        return r[0] <= count <= r[1]

def solution(input, part2):
    valid_passwords = 0
    for i in input:
        result = is_valid(i, part2)
        if result:
            valid_passwords += 1
    return valid_passwords



example_input = get_input(example_file)
exercise_input = get_input(exercise_file)

print(solution(example_input, False)) #2
print(solution(exercise_input, False)) #493 #32
print(solution(example_input, True)) #1
print(solution(exercise_input, True)) #593 #20