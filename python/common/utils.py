
def print_solution(question, example_answer, example_expected, answer):
    print("D{} ".format(question) + "*" * 96)
    print("\texample = {0} {1}\n\tanswer = {2}".format(
        example_answer, "GOOD" if example_answer == example_expected else "WRONG",
        answer))
    print("*"*100)

def print_solution2(question, answers, expecteds):
    length = 100
    print("D{} ".format(question) + "*" * (length - 2 - len(question)))
    analyse("Part1", answers[0], expecteds[0])
    analyse("Part2", answers[1], expecteds[1])
    print("*" * length)

def analyse(part, answer, expected):
    operator = "==" if answer == expected else "!="
    message = "OK" if answer == expected else "WRONG"
    print("\t{0}:  {1} {2} {3} {4}".format(part, answer, operator, expected, message))
