from ..common.utils import print_solution

exercise = "xx"
example = "{}ex".format(exercise)

def read_input(file_name):
    data = []
    file = open(r"..\data\{0}.txt".format(file_name))
    for line in file:
        data.append(line.strip())
        #elements = line.split()
        #data.append((elements[0], elements[1]))
    return data


def q1_solution():
    example_expected = 0
    example_answer = q1(example)
    answer = -1 #q1(exercise)
    print_solution(1, example_expected, example_answer, answer)

def q2_solution():
    example_expected = 0
    example_answer = q2(example)
    answer = -1 #q2(exercise)
    print_solution(2, example_expected, example_answer, answer)


def q1(file_name):
    data = read_input(file_name)
    answer = 0
    return answer

def q2(file_name):
    data = read_input(file_name)
    answer = 0
    return answer

def run():
    q1_solution()
    #q2_solution()

def main():
    try:
        run()
    except Exception as e:
        print("Run failed due to {}".format(e))
main()