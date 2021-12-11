from common.utils import print_solution

exercise = "06"
example = "{}ex".format(exercise)


def read_input(file_name):
    data = []
    file = open(r"..\data\{0}.txt".format(file_name))
    for line in file:
        elements = line.strip().split(",")
        data = [int(i) for i in elements]
    return data


def q1_solution():
    example_expected = 5934
    example_answer = q1(example, 80)
    answer = q1(exercise, 80)
    print_solution(1, example_expected, example_answer, answer)


def q2_solution():
    example_expected = 26984457539 #26  # 5934 #26984457539
    example_answer = q2(example, 256) #18#80#256
    answer = q2(exercise, 256)
    print_solution(2, example_expected, example_answer, answer)


def q1(file_name, days):
    fishies = read_input(file_name)
    for day in range(days):
        new_fish = 0
        for i in range(len(fishies)):
            if fishies[i] != 0:
                fishies[i] -= 1
            elif fishies[i] == 0:
                fishies[i] = 6
                new_fish += 1
        for x in range(new_fish):
            fishies.append(8)

    return len(fishies)


def q2(file_name, days):
    fishies = read_input(file_name)
    fish_map = {}
    for fish in fishies:
        if fish not in fish_map.keys():
            fish_map[fish] = 1
        else:
            fish_map[fish] += 1

    for day in range(days):
        new_fish_map = {}
        for age, num_fish in fish_map.items():
            if age != 0:
                new_fish_map[age - 1] = num_fish

        if 0 in fish_map.keys():
            if 6 not in new_fish_map.keys():
                new_fish_map[6] = 0
            new_fish_map[6] = new_fish_map[6] + fish_map[0]
            new_fish_map[8] = fish_map[0]

        fish_map = new_fish_map

    total = 0
    for num_fish in fish_map.values():
        total += num_fish

    return total


def run():
    # q1_solution()
    q2_solution()


def main():
    try:
        run()
    except Exception as e:
        print("Run failed due to {}".format(e))


main()
