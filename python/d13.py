from common.utils import print_solution2
from collections import Counter, defaultdict
import numpy as np
from pprint import pprint

day = "13"
exercise_file = r"..\data\{0}.txt".format(day)
example_file = r"..\data\{0}ex.txt".format(day)
answers = (-1, -1)
example_answers = answers

def get_input(input_file):
    coords = []
    folds = []
    fold_along = "fold along"
    for line in open(input_file):
        if "," in line:
            coords.append([int(i) for i in line.strip().split(',')])
        elif line.startswith(fold_along):
            fold = line.removeprefix(fold_along).strip().split("=")
            folds.append([fold[0], int(fold[1])])

    return coords, folds

def create_plot(coords):
    x_size = max([c[0] for c in coords])
    y_size = max([c[1] for c in coords])
    size = (y_size + 1, x_size + 1)
    plot = np.zeros(size)
    for x, y in coords:
        plot[y, x] = 1
    return plot

def create_test_plot(coords):
    x_size = max([x for x in coords[0]])
    y_size = max([y for y in coords[1]])
    size = (y_size + 1, x_size + 1)
    plot = np.zeros(size)
    counter = 0
    for y in range(size[0]):
        for x in range(size[1]):
            counter += 1
            plot[y, x] = counter
    return plot

def sub_matrix(matrix, y1, y2, x1, x2):
    new_size = (y2 - y1 + 1, x2 - x1 + 1)
    new_matrix = np.zeros(new_size)
    for ny, y in enumerate(range(y1, y2 + 1)):
        for nx, x in enumerate(range(x1, x2 + 1)):
            new_matrix[ny, nx] = matrix.item(y, x)
    return new_matrix

def fold_vertical(matrix, x_size):
    assert matrix.shape[1] % 2 == 1 # must be odd for this to work?
    y_size = matrix.shape[0]
    new_size = (y_size, x_size)
    left = np.zeros(new_size)
    right = np.zeros(new_size)

    for y in range(y_size):
        for x in range(x_size):
            left[y, x] = matrix.item(y, x)
    # print("folded left = ")
    # pprint(left)

    for ny, y in enumerate(range(y_size)):
        for nx, x in enumerate(range(matrix.shape[1] - 1, x_size, -1)):
            item = matrix.item(y, x)
            right[ny, nx] = item
    # print("folded right = ")
    # pprint(right)
    return left, right

def fold_horizontal(matrix, y_size):
    assert matrix.shape[0] % 2 == 1 # must be odd for this to work?
    x_size = matrix.shape[1]
    new_size = (y_size, x_size)
    new_matrix = np.zeros(new_size)
    mirror_matrix = np.zeros(new_size)

    for y in range(y_size):
        for x in range(x_size):
            new_matrix[y, x] = matrix.item(y, x)
    # print("folded top = ")
    # pprint(new_matrix)

    for ny, y in enumerate(range(matrix.shape[0] - 1, y_size, -1)):
        for nx, x in enumerate(range(x_size)):
            item = matrix.item(y, x)
            mirror_matrix[ny, nx] = item
    # print("folded bottom = ")
    # pprint(mirror_matrix)
    return new_matrix, mirror_matrix

def fold_generic(matrix, y, x):
    raise Exception("TODO: implement")

def process_folds(plot, folds):
    print("folding")
    for n, fold in enumerate(folds):
        if fold[0] == 'y':
            top, bottom = fold_horizontal(plot, fold[1])
            new_plot = top + bottom
            plot = new_plot
        elif fold[0] == 'x':
            left, right = fold_vertical(plot, fold[1])
            new_plot = left + right
            plot = new_plot
    return n, plot

def solution_part1(input_file):
    coords, folds = get_input(input_file)
    plot = create_plot(coords)
    n, plot = process_folds(plot, [folds[0]]) #only process the first fold
    print("after ", n, " folds the result is ", np.count_nonzero(plot))
    pprint(plot)

def write_code(plot):
    print("code: ")
    for y in range(plot.shape[0]):
        row = ""
        for x in range(plot.shape[1]):
            row += "#" if plot.item(y, x) >= 1 else " "
        print(row)
        #CPZLPFZL

#Since I'm on the plane and I don't have part 2 I'm going to guess it: process all folds
def solution_part2_guess(input_file):
    coords, folds = get_input(input_file)
    plot = create_plot(coords)
    n, plot = process_folds(plot, folds) #only process the first fold
    print("after ", n, " folds the result is ", np.count_nonzero(plot))
    pprint(plot.shape)
    write_code(plot)



# solution_part1(example_file) #correct = 17
# solution_part2_guess(example_file) #correct = 16

#solution_part1(exercise_file) #correct = 607 ???
solution_part2_guess(exercise_file) #correct = 87 ??? #CPZLPFZL