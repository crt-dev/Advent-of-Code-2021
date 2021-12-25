from common.utils import print_solution2
from collections import Counter, defaultdict, deque
import numpy as np
from pprint import pprint

day = "12"
exercise_file = r"..\data\{0}.txt".format(day)
example_file = r"..\data\{0}ex.txt".format(day)

def get_input(input_file):
    input = [x.strip().split("-") for x in open(input_file)]
    return input

def create_cave_map(input):
    cave_map = defaultdict(set)
    for v1, v2 in input:
        cave_map[v1].add(v2)
        cave_map[v2].add(v1)
    return cave_map

def solution(input_file):
    input = get_input(input_file)
    cave_map = create_cave_map(input)
    pprint(cave_map)

    start = ("start", ["start"], ["start"]) #current location, visited locations
    queue = deque([start])
    count = 0
    while queue:
        location, restrictions, history = queue.pop()
        if location == "end":
            count += 1
            print("completed route ", count, ": ", history)
            continue
        available_destinations = cave_map[location]
        for destination in available_destinations:
            if destination not in restrictions:
                new_history = history[:]
                new_history.append(destination)
                new_restrictions = restrictions[:]
                if destination.lower() == destination:
                    new_restrictions.append(destination)
                entry = (destination, new_restrictions, new_history)
                queue.append(entry)

    print("Route plotting complete with {} paths found".format(count))

def solution2(input_file):
    input = get_input(input_file)
    cave_map = create_cave_map(input)
    pprint(cave_map)

    start = ("start", ["start"], ["start"], False) #current location, visited locations
    queue = deque([start])
    count = 0
    while queue:
        location, restrictions, history, double_visit = queue.popleft()
        if location == "end":
            count += 1
            print("completed route ", count, ": ", history)
            continue
        available_destinations = cave_map[location]
        for destination in available_destinations:
            if destination not in restrictions:
                new_history = history[:]
                new_history.append(destination)
                new_restrictions = restrictions[:]
                if destination.lower() == destination:
                    if not double_visit:
                        double_visit = True
                    else:
                        new_restrictions.append(destination)
                entry = (destination, new_restrictions, new_history, double_visit)
                queue.append(entry)

    print("Route plotting complete with {} paths found".format(count))

def solution3(input_file):
    input = get_input(input_file)
    cave_map = create_cave_map(input)
    pprint(cave_map)

    start = ("start", ["start"], ["start"], False) #current location, visited locations
    queue = deque([start])
    count = 0
    while queue:
        location, restrictions, history, double_visit = queue.popleft()
        if location == "end":
            count += 1
            print("completed route ", count, ": ", history)
            continue
        available_destinations = cave_map[location]
        for destination in available_destinations:
            if destination not in restrictions:
                new_history = history[:]
                new_history.append(destination)
                new_restrictions = restrictions[:]
                if destination.lower() == destination:
                    new_restrictions.append(destination)
                entry = (destination, new_restrictions, new_history, double_visit)
                queue.append(entry)
            elif destination in restrictions and double_visit == False and destination not in ["start", "end"]:
                new_history = history[:]
                new_history.append(destination)
                queue.append((destination, restrictions, new_history, True))

    print("Route plotting complete with {} paths found".format(count))

#solution(example_file) #10
#solution(exercise_file) #5212

#solution3(example_file) #36
solution3(exercise_file) #134862
