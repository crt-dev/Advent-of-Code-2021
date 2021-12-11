from common.utils import print_solution2

day = "11"
exercise_file = r"..\data\{0}.txt".format(day)
example_file = r"..\data\{0}ex.txt".format(day)
answers = (0, 0)
example_answers = (0, 0)

error_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

open_chars = ['(', '[', '{', '<']
close_chars = [')', ']', '}', '>']
char_map = dict(zip(open_chars, close_chars))

def get_auto_score(chars):
    score = 0
    for c in chars:
        score = score*5
        score += autocomplete_score[c]
    return score

def solution(input_file):
    input = [x.strip() for x in open(input_file)]
    part1_score = 0
    part2_scores = []

    for line in input:
        queue = []
        broken = False
        for c in line:
            if c in open_chars:
                queue.append(char_map[c])
            elif c in close_chars:
                if not queue or c != queue.pop():
                    part1_score += error_score[c]
                    broken = True
            else:
                raise Exception("Unexpected char ", c)
        if len(queue) != 0 and broken is False: #incomplete
            auto_score = get_auto_score(reversed(queue))
            part2_scores.append(auto_score)
            #print(queue, auto_score)

    #print("error chars = ", error_chars)
    part2_scores.sort()
    target = len(part2_scores)//2
    return part1_score, part2_scores[target]


example_answers = solution(example_file)
answers = solution(exercise_file)

print_solution2(day + "ex", example_answers, [26397, 288957])
print_solution2(day, answers, [323691, 2858785164])
