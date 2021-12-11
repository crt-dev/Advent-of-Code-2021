from common.utils import print_solution2
from collections import Counter, defaultdict
import numpy as np

day = "12"
exercise_file = r"..\data\{0}.txt".format(day)
example_file = r"..\data\{0}ex.txt".format(day)
answers = (-1, -1)
example_answers = answers

def get_input(input_file):
    input = [x.strip() for x in open(input_file)]
    return input

def solution(input_file):
    input = [] #get_input(input_file)
    p1_answer = 0
    p2_answer = -1
    return p1_answer, p2_answer


example_answers = solution(example_file)
#answers = solution(exercise_file)

print_solution2(day + "ex", example_answers, [-1, -1])
#print_solution2(day, answers, [-1, -1])
