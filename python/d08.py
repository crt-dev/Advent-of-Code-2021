from collections import Counter, defaultdict

exercise = r"..\data\08.txt"
example = r"..\data\08ex.txt"
example2 = r"..\data\08ex2.txt"

def read_input(input_file):
    input = []
    for line in open(input_file):
        elements = line.strip().split('|')
        digits = elements[1].split()
        input.append(digits)
    return input

def solution(input_file):
    input = read_input(input_file)
    output = defaultdict(int)
    basic_count = 0
    target = [2,3,4,7]

    inc = 0
    for line in input:
        line_count = 0
        for digit in line:
            counter = Counter(c for c in digit)
            count = len(counter)
            if count in target:
                output[count] += 1
                line_count += 1
        basic_count += line_count
        print(inc, " ", line_count)
        inc += 1

    return sum(output.values())

#In the output values, how many times do digits 1, 4, 7, or 8 appear?

#print(solution(example)) #
#print(solution(example2))
print(solution(exercise))