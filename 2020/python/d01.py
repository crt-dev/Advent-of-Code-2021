from collections import Counter, defaultdict
import numpy as np
from pprint import pprint
from itertools import permutations

day = "01"
exercise_file = r"..\data\d{0}.txt".format(day)
example_file = r"..\data\d{0}eg.txt".format(day)

def get_input(input_file):
    input = [int(x.strip()) for x in open(input_file)]
    return input

def solution(input, items):
    perms = list(permutations(input, items))
    for p in perms:
        if sum(p) == 2020:
            return np.prod(p)
    raise Exception("no 2020 sum found")

example_input = get_input(example_file)
exercise_input = get_input(exercise_file)

print(solution(example_input, 2)) #514579
print(solution(exercise_input, 2)) #910539 #13
print(solution(example_input, 3)) #514579
print(solution(exercise_input, 3)) #910539 #3