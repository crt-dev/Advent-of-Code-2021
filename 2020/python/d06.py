from collections import Counter

day = "06"
exercise_file = r"..\data\d{0}.txt".format(day)
example_file = r"..\data\d{0}eg.txt".format(day)

def get_input(input_file):
    input = []
    answers = []
    for line in open(input_file):
        if line == "\n":
            input.append(answers)
            answers = []
        else:
            answers.append(line.strip())
    input.append(answers)
    return input


def solution_p1(input):
    size = 0
    for group in input:
        group_answers = set(answer for person in group for answer in person)
        size += len(group_answers)
    return size


def solution_p2(input):
    size = 0
    for group in input:
        joined = "".join(group)
        count = Counter(joined)
        filtered = {key: value for key, value in count.items() if value == len(group)}
        size += len(filtered)
    return size

example_input = get_input(example_file)
exercise_input = get_input(exercise_file)

print(solution_p1(example_input)) #11
print(solution_p1(exercise_input)) #6585
print(solution_p2(example_input)) #6
print(solution_p2(exercise_input)) #3276