from common.utils import print_solution2
from collections import Counter, defaultdict
import numpy as np

day = "11"
exercise_file = r"..\data\{0}.txt".format(day)
example_file = r"..\data\{0}ex.txt".format(day)
answers = (-1, -1)
example_answers = answers

trans_x = [0, 1, 1, 1, 0, -1, -1, -1]
trans_y = [1, 1, 0, -1, -1, -1, 0, 1]

def get_example_input():
    return [
        [1, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 9, 1, 9, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 1, 1]
    ]

def get_input(input_file):
    input = []
    for line in open(input_file):
        row = []
        for c in line.strip():
            row.append(int(c))
        input.append(row)

    return input

def solution(input_file, steps):
    input = get_input(input_file)
    octopus = np.matrix(input)
    flashes = 0
    all_flash = None
    for s in range(steps):
        flash_register = set()
        octopus += 1
        shiners = np.where(octopus > 9)
        while len(shiners[0]) != 0:
            for y, x in zip(shiners[0], shiners[1]):
                if (y, x) not in flash_register:
                    for n, ty in enumerate(trans_y):
                        dy = y + ty
                        dx = x + trans_x[n]
                        if 0 <= dy < octopus.shape[0] and 0 <= dx < octopus.shape[1]:
                            if (dy, dx) not in flash_register:
                                octopus[dy, dx] += 1
                    octopus[y, x] = 0
                    flashes += 1
                    flash_register.add((y, x))
            shiners = np.where(octopus > 9)

        if octopus.sum() == 0:
            all_flash = s + 1
            break

    return flashes, all_flash

example_answers = solution(example_file, 100)
answer_p1 = solution(exercise_file, 100)
answer_p2 = solution(exercise_file, 1000)

print_solution2(day + "ex", example_answers, [1656, None])
print_solution2(day + " p1", answer_p1, (1747, None))
print_solution2(day + " p2", answer_p2, (8282, 505))