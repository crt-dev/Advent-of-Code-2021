from collections import Counter, defaultdict
import numpy as np
from pprint import pprint
from itertools import permutations
import math

day = "05"
exercise_file = r"..\data\d{0}.txt".format(day)
example_file = r"..\data\d{0}eg.txt".format(day)


def get_input(input_file):
    input = [x.strip() for x in open(input_file)]
    return input


def binary_search(code, smin, smax):
    pos = 0
    while smin != smax and pos <= len(code):
        c = code[pos]
        if c in {'F', 'L'}:
            smax = int((smax + smin)/2)
        elif c in {'B', 'R'}:
            smin = math.ceil((smax + smin)/2)
        pos += 1

    assert smin == smax
    return smax


def get_seats(input):
    seats = []
    for seat_code in input:
        row_code = seat_code[:7]
        column_code = seat_code[7:]
        row = binary_search(row_code, 0, 127)
        col = binary_search(column_code, 0, 7)
        seats.append((row, col))
    return seats


def get_seat_id(row, col):
    return row * 8 + col


def solution(input):
    seat_ids = []
    for row, col in get_seats(input):
        seat_ids.append(get_seat_id(row, col))
    return max(seat_ids)

#Quick and dirty way to get to a solution via visual inspection
def solution_part2(input):
    size = (128, 8)
    plan = np.zeros(size)
    for row, col in get_seats(input):
        plan[row][col] = 1

#Let's try solving this programmatically
def solution_part2b(input):
    seat_plan = set(list(range(1023)))
    for row, col in get_seats(input):
        seat_plan.remove(get_seat_id(row, col))

    empty_seats = list(seat_plan)
    for i in range(1, len(empty_seats)):
        if empty_seats[i - 1] != empty_seats[i] - 1 and empty_seats[i + 1] != empty_seats[i] + 1:
            return empty_seats[i]
    raise Exception("Could not find seat")


#example_input = ["FBFBBFFRLR"]
example_input = get_input(example_file)
exercise_input = get_input(exercise_file)

print(solution(example_input)) #820
print(solution(exercise_input)) #878 37
#solution_part2(exercise_input) #504 #47
print(solution_part2b(exercise_input))