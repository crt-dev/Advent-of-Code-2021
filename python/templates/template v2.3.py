from collections import Counter, defaultdict
import numpy as np
from pprint import pprint

day = "xx"
exercise_file = r"..\data\d{0}.txt".format(day)
example_file = r"..\data\d{0}eg.txt".format(day)

def get_input(input_file):
    input = [x.strip() for x in open(input_file)]
    return input

def solution(input):
    answer = input[0]
    return answer

example_input = get_input(example_file)
exercise_input = get_input(exercise_file)

print(solution(example_input)) #
print(solution(exercise_input)) #