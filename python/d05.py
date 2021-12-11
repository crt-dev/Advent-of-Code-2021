from common.utils import print_solution
import numpy

exercise = "05"
example = "{}ex".format(exercise)

def read_input(file_name):
    data = []
    file = open(r"..\data\{0}.txt".format(file_name))
    for line in file:
        elements = line.strip().split("->")
        coords = []
        for element in elements:
            coords.extend(int(x) for x in element.split(","))
        data.append(coords)
    return data


def q1_solution():
    example_expected = 5
    example_answer = q1(example)
    answer = q1(exercise) #7085
    print_solution(1, example_expected, example_answer, answer)


def q2_solution():
    example_expected = 12
    example_answer = q2(example)
    answer = q2(exercise) #20271
    print_solution(2, example_expected, example_answer, answer)


def get_lines(data):
    horizontal_lines = []
    vertical_lines = []
    diagonal_lines = []
    for line in data:
        if line[0] == line[2]:
            vertical_lines.append(line)
        elif line[1] == line[3]:
            horizontal_lines.append(line)
        else:
            diagonal_lines.append(line)
    return horizontal_lines, vertical_lines, diagonal_lines


def plot_horizontal(lines, area_map):
    for line in lines:
        if line[2] < line[0]:
            horizontal_range = range(line[2], line[0]+1)
        else:
            horizontal_range = range(line[0], line[2]+1)
        for x in horizontal_range:
            area_map[line[1]][x] += 1


def plot_vertical(lines, area_map):
    for line in lines:
        if line[3] < line[1]:
            vertical_range = range(line[3], line[1]+1)
        else:
            vertical_range = range(line[1], line[3]+1)
        for y in vertical_range:
            area_map[y][line[0]] += 1


def plot_diagonal(lines, area_map):
    for line in lines:
        if line[2] > line[0]:
            x_range = range(line[0], line[2]+1)
        else:
            x_range = range(line[0], line[2]-1, -1)

        if line[3] > line[1]:
            y_range = range(line[1], line[3]+1)
        else:
            y_range = range(line[1], line[3]-1, -1)

        coords = []
        x_range = list(x_range)
        y_range = list(y_range)
        assert (len(x_range) == len(y_range))

        for i in range(len(x_range)):
            coords.append((x_range[i], y_range[i]))

        for coord in coords:
            area_map[coord[1]][coord[0]] += 1

def q1(file_name):
    data = read_input(file_name)
    data_matrix = numpy.matrix(data)
    s = (data_matrix.max() + 1, data_matrix.max() + 1)
    area_map = numpy.zeros(s)

    horizontal_lines, vertical_lines, ignore_lines = get_lines(data)
    plot_horizontal(horizontal_lines, area_map)
    plot_vertical(vertical_lines, area_map)

    return numpy.count_nonzero(area_map >= 2)

def q2(file_name):
    data = read_input(file_name)
    data_matrix = numpy.matrix(data)
    s = (data_matrix.max() + 1, data_matrix.max() + 1)
    area_map = numpy.zeros(s)

    horizontal_lines, vertical_lines, diagonal_lines = get_lines(data)
    plot_horizontal(horizontal_lines, area_map)
    plot_vertical(vertical_lines, area_map)
    plot_diagonal(diagonal_lines, area_map)

    return numpy.count_nonzero(area_map >= 2)

def run():
    q1_solution()
    q2_solution()

def main():
    try:
        run()
    except Exception as e:
        print("Run failed due to {}".format(e))
main()