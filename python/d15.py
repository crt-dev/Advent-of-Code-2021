from collections import Counter, defaultdict
import numpy as np
from pprint import pprint
from collections import deque
from copy import deepcopy
import heapq

day = "15"
exercise_file = r"..\data\{0}.txt".format(day)
example_file = r"..\data\{0}ex.txt".format(day)

def get_input(input_file):
    input = [[int(n) for n in line.strip()] for line in open(input_file)]
    return input

def solution_attempt_1(input_file):
    #MCP approach which works for the example but fails to find the optimal path for exercise input
    risk = get_input(input_file)
    size = len(risk)
    assert(size == len(risk[0]))

    total_risk = [[0 for x in range(size)] for x in range(size)]
    for i in range(1, size):
        total_risk[i][0] = total_risk[i - 1][0] + risk[i][0]
        total_risk[0][i] = total_risk[0][i - 1] + risk[0][i]

    for i in range(1, size):
        for j in range(1, size):
            total_risk[i][j] = min(total_risk[i-1][j], total_risk[i][j-1]) + risk[i][j]

    #pprint(total_risk)
    check = np.matrix(total_risk)
    return total_risk[size -1][size - 1]

def solution2(input_file):
    risk = get_input(input_file)
    risk[0][0] = 0
    size = len(risk)
    assert(size == len(risk[0]))

    min_risk = 0
    for n in range(size):
        min_risk += risk[n][n] #just pick any value for initial minimum
    q_pops = 0

    total_risks = []
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    start = (0, 0, 0, set([(0, 0)]))
    q = deque([start])
    while q:
        q_pops += 1
        if q_pops % 5000 == 0:
            print("q_pops = ", q_pops)

        i, j, current_risk, history = q.pop()
        if min_risk and current_risk > min_risk:
            continue

        if i == size - 1 and j == size - 1:
            total_risk = current_risk + risk[i][j]
            total_risks.append(total_risk)
            min_risk = min(total_risks)
            print("found path with total risk {} (min={}, q.size={})".format(total_risk, min_risk, len(q)))
            continue

        for n, d in enumerate(dx):
            x = i + dx[n]
            y = j + dy[n]
            if 0 <= x < size and 0 <= y < size:
                if (x, y) not in history:
                    new_history = deepcopy(history)
                    new_history.add((x, y))
                    q.append((x, y, current_risk + risk[x][y], new_history))

    print("found {} paths", len(total_risks))
    return min_risk

def add_matrix_2_matrix(destination, source, start_x, start_y):
    for j in range(source.shape[0]):
        for i in range(source.shape[1]):
            if 0 < j <= destination.shape[0] and 0 < i <= destination.shape[1]:
                destination[start_y + j, start_x + i] = source.item(j, i)

def transform_input(input, multiple):
    size = (len(input), len(input[0]))
    new_size = (size[0] * multiple, size[1] * multiple)
    output = np.zeros(new_size)

    for j in range(multiple):
        for i in range(multiple):
            add_matrix_2_matrix(output, np.multiply(input, j + i + 1), j * size[1],  i * size[0])

    output2 = [[None for _ in range(new_size[0])] for _ in range(new_size[0])]
    for j in range(new_size[0]):
        for i in range(new_size[1]):
            value = output.item(j, i)
            while value > 9:
                value -= 9
            output2[i][j] = output.item(j, i)

    return output2

def solution3(input_file, transform_input_flag = False):
    risk = get_input(input_file)
    if transform_input_flag:
        risk = transform_input(risk, 5)
    size = len(risk)
    assert(size == len(risk[0]))
    total_risk = [[None for _ in range(size)] for _ in range(size)]

    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    start = (0, 0, 0)
    q = [start]
    q_pops = 0
    while q:
        q_pops += 1
        if q_pops % 5000 == 0:
            print("q_pops = ", q_pops)

        (dist, x, y) = heapq.heappop(q)
        if x < 0 or x >= size or y < 0 or y >= size:
            continue

        value = risk[x][y]
        cost = dist + value

        if total_risk[x][y] is None or cost < total_risk[x][y]:
            total_risk[x][y] = cost
        else: continue

        for d, dd in enumerate(dx):
            tx = x + dx[d]
            ty = y + dy[d]
            heapq.heappush(q, (total_risk[x][y], tx, ty))

    return total_risk[size - 1][size - 1] - risk[0][0]

#print(solution(example_file)) #40
#print(solution(exercise_file)) #393 (396)

#print(solution2(example_file)) #40
#print(solution2(exercise_file)) #393 (396)

print(solution3(example_file, True)) #
# print(solution3(exercise_file)) #

#393
#2823