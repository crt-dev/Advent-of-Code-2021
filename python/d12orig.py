from common.utils import print_solution2
from collections import Counter, defaultdict, deque
import numpy as np
import itertools
from pprint import pprint


day = "12"
exercise_file = r"..\data\{0}.txt".format(day)
example_file = r"..\data\{0}ex.txt".format(day)
answers = (-1, -1)
example_answers = answers


def get_input(input_file):
    input = [x.strip().split("-") for x in open(input_file)]
    return input

def create_cave_map(input):
    cave_map = defaultdict(set)
    for location, connection in input:
        cave_map[location].add(connection)
        cave_map[connection].add(location)
    return cave_map

master = []
def navigate_to(cave_map, position, visited, route):
    route.append(position)
    if position == "end":
        print("I'm at the end so I'm done")
        master.append(route[:])
        route.pop()
    else:
        if position.islower():
            visited.add(position)
        options = cave_map[position]
        options = options.difference(visited)
        if len(options) != 0:
            print("I'm in ", position, " with options of ", options)
            for i in options:
                navigate_to(cave_map, i, visited, route)
        else:
            print("I'm in ", position, " which is a dead end")
            route.pop()

def my_plot_routes(cave_map, param):
    start = ('start', set(['start']))
    routes = 0
    queue = deque([start])
    while queue:
        position, visited = queue.popleft()
        if position == 'end':
            routes += 1
            continue
        for p in cave_map[position]:
            if p not in visited:
                new_visted = set(visited)
                if p.lower() == p:
                    new_visted.add(p)
                queue.append((p, new_visted))
            elif p in visited and p not in ['start', 'end']:
                queue.append((p, visited))


    return routes


def solution(input_file):
    input = get_input(input_file)
    cave_map = create_cave_map(input)
    print(my_plot_routes(cave_map, True))


solution(example_file)

def plot_routes(cave_map, param):
    start = ('start', set(['start']), None)
    answer = 0
    queue = deque([start])
    while queue:
        pos, small, twice = queue.popleft()
        if pos == 'end':
            answer += 1
            continue
        for y in cave_map[pos]:
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                queue.append((y, new_small, twice))
            elif y in small and twice is None and y not in ['start', 'end'] and not param:
                queue.append((y, small, y))
    return answer
