from collections import defaultdict, Counter

exercise = "06"
example = "{}ex".format(exercise)

def solution(file_name, days):
    fishies = Counter([int(x) for x in open(r"..\data\{0}.txt".format(file_name)).read().strip().split(',')])
    fish_map = fishies
    for day in range(days):
        new_fish_map = defaultdict(int)
        for age, num_fish in fish_map.items():
            if age == 0:
                new_fish_map[6] += num_fish
                new_fish_map[8] += num_fish
            else:
                new_fish_map[age - 1] += num_fish

        fish_map = new_fish_map

    return sum(fish_map.values())

print(solution(example, 18))
print(solution(example, 80))
print(solution(exercise, 80))
print(solution(example, 256))
print(solution(exercise, 256))