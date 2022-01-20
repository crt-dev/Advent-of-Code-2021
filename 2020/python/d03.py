day = "03"
exercise_file = r"..\data\d{0}.txt".format(day)
example_file = r"..\data\d{0}eg.txt".format(day)

def get_input(input_file):
    input = [x.strip() for x in open(input_file)]
    return input

def count_trees(input, across, down):
    px = 0
    py = 0
    trees = 0
    width = len(input[0])

    while py < len(input) - 1:
        px += across
        py += down
        if input[py][px % width] == '#':
            trees += 1

    return trees

def part2(input):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    trees = []
    answer = 1
    for slope in slopes:
        trees.append(count_trees(input, slope[0], slope[1]))
        answer = answer * trees[-1]

    #return np.prod(trees)
    return answer


example_input = get_input(example_file)
exercise_input = get_input(exercise_file)

print(count_trees(example_input, 3, 1)) #7
print(count_trees(exercise_input, 3, 1)) #259 #31
print(part2(example_input)) #336
print(part2(exercise_input)) #2224913600 #15