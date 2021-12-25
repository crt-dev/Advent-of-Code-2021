from collections import Counter, defaultdict
import numpy as np
from pprint import pprint

day = "15"
exercise_file = r"..\data\{0}.txt".format(day)
example_file = r"..\data\{0}ex.txt".format(day)

def get_input(input_file):
    input = [x.strip() for x in open(input_file)]
    return input

def solution(input_file):
    input = [] #get_input(input_file)
    answer = 0
    return answer


print(solution(example_file)) #
#print(solution(exercise_file)) #