def process(line):
    line_elements = line.split()
    return line_elements[0], int(line_elements[1])


def read_input(file_name):
    data = []
    file = open(r"..\data\{0}.txt".format(file_name))
    for line in file:
        data.append(process(line))
    return data


def q1(file_name):
    data = read_input(file_name)
    return 0


def q2(file_name):
    data = read_input(file_name)
    return 0


def run():
    exercise = "xx"
    example = "{}ex".format(exercise)
    q1_ex_expected = 0
    q2_ex_expected = 0
    ans_q1ex = q1(example)
    ans_q1 = q1(exercise)
    ans_q2ex = q2(example)
    ans_q2 = q2(exercise)

    print("*"*100)
    print("\tq1ex = {0} {1}\n\tq1 = {2}\n\tq2ex = {3} {4}\n\tq2 = {5}".format(
        ans_q1ex, "EXPECTED" if ans_q1ex == q1_ex_expected else "WRONG", ans_q1,
        ans_q2ex, "EXPECTED" if ans_q2ex == q2_ex_expected else "WRONG", ans_q2))
    print("*"*100)

def main():
    try:
        run()
    except Exception as e:
        print("Run failed due to {}".format(e))
main()

