from collections import Counter, defaultdict
import numpy as np
from pprint import pprint

day = "19"
exercise_file = r"..\data\d{0}.txt".format(day)
example_file = r"..\data\d{0}eg.txt".format(day)

def get_input(input_file):
    input = {}
    scanner = None
    for line in open(input_file):
        if line.startswith("---"):
            scanner = int(line[12:-4])
            input[scanner] = []
        elif len(line) > 2:
            coords = [int(n) for n in line.strip().split(",")]
            input[scanner].append(coords)

    return input

def solution(input):
    answer = input[0]
    return answer

#example_input = get_input(example_file) #89 beacons
exercise_input = get_input(exercise_file)

#print(solution(example_input)) #
print(solution(exercise_input)) #