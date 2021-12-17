from collections import Counter, defaultdict
from math import ceil

day = "14"
exercise_file = r"..\data\{0}.txt".format(day)
example_file = r"..\data\{0}ex.txt".format(day)


def get_input(input_file):
    delimiter = " -> "
    rules = defaultdict(str)
    for line in open(input_file):
        if delimiter not in line and len(line) >= 2:
            template = line.strip()
        elif delimiter in line:
            rule = line.strip().split(delimiter)
            rules[rule[0]] = rule[1]

    return template, rules


def solution(input_file, steps):
    template, rules = get_input(input_file)
    t = [c for c in template]
    for s in range(steps):
        insertions = []
        for i in range(1, len(t)):
            r = t[i - 1] + t[i]
            if r in rules.keys():
                insertions.append((rules[r], i + len(insertions)))
        for i in insertions:
            t.insert(i[1], i[0])

    count = Counter(c for c in t)
    return max(count.values()) - min(count.values())


def solution2(input_file, steps):
    template, rules = get_input(input_file)
    t = [c for c in template]
    pairs = dict(Counter(t[i - 1] + t[i] for i in range(1, len(t))))

    for s in range(steps):
        new_pairs = defaultdict(int)
        for key, n in pairs.items():
            if key in rules.keys():
                new_key1 = key[0] + rules[key]
                new_key2 = rules[key] + key[1]
                new_pairs[new_key1] += n
                new_pairs[new_key2] += n
        pairs = new_pairs

    count = defaultdict(int)
    for key, n in pairs.items():
        count[key[0]] += n
        count[key[1]] += n

    cmax = max(count.values())
    cmin = min(count.values())
    return ceil(cmax / 2) - ceil(cmin / 2)  # hack to adjust for counting letters twice


# print(solution(example_file, 10)) #1588
# print(solution(exercise_file, 10)) #2375

# print(solution2(example_file, 10)) #1588
# print(solution2(exercise_file, 10)) #2375
print(solution2(example_file, 40))  # 2188189693529
print(solution2(exercise_file, 40))  # 1976896901756
