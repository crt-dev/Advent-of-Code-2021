from common.utils import print_solution
import numpy

exercise = "04"
example = "{}ex".format(exercise)

def read_input(file_name):
    rounds = []
    boards = []
    markings = []
    file = open(r"..\data\{0}.txt".format(file_name))
    board = []
    for line in file:
        if len(rounds) == 0:
            rounds = [int(x) for x in  line.strip().split(",")]
        else:
            if len(line) < 2:
                if len(board) != 0:
                    boards.append(board)
                    markings.append(numpy.zeros((5,5)))
                board = []
            else:
                board.append([int(x) for x in line.strip().split()])

    boards.append(board)
    markings.append(numpy.zeros((5,5)))

    print("Finished reading {} boards {} rounds".format(len(boards), len(rounds)))
    return rounds, boards, markings


def q1_solution():
    example_expected = 4512
    example_answer = 4512 #q1(example)
    #answer = 0
    answer = q1(exercise)
    print_solution(1, example_expected, example_answer, answer)

def q2_solution():
    example_expected = 1924
    example_answer = q2(example)
    answer = q2(exercise)
    print_solution(2, example_expected, example_answer, answer)


def process_round(round, boards, markings):
    for n in range(len(boards)):
        for i in range(5):
            for j in range(5):
                if boards[n][i][j] == round:
                    markings[n][i][j] = 1
    print("finished scoring round ", round)

def is_winner(marking):
    for i in marking.T:
        if sum(i) == 5:
            return True

    for i in marking:
        if sum(i) == 5:
            return True

    return False

def get_score(board, marking, winning_round):
    board_sum = 0
    for i in range(5):
        for j in range(5):
            if marking[i][j] == 0:
                board_sum += board[i][j]
    return board_sum * winning_round

def q1(file_name):
    rounds, boards, markings = read_input(file_name)
    assert(len(boards) in (3,100))
    assert(len(markings) in (3,100))
    for round in rounds:
        process_round(round, boards, markings)
        for n in range(len(boards)):
            if is_winner(markings[n]):
                score = get_score(boards[n], markings[n], round)
                return score
    raise Exception("No winner found")

def q2(file_name):
    rounds, boards, markings = read_input(file_name)
    assert(len(boards) in (3,100))
    assert(len(markings) in (3,100))
    winners = set()
    win_record = []
    for round in rounds:
        process_round(round, boards, markings)
        for n in range(len(boards)):
            if is_winner(markings[n]):
                if n not in winners:
                    winners.add(n)
                    score = get_score(boards[n], markings[n], round)
                    win_record.append(score)
                    print("Found winning board {} at position {} and round {}".format(n, len(win_record), round))
    return win_record[-1]

def run():
    #q1_solution()
    q2_solution()

def main():
    try:
        run()
    except Exception as e:
        print("Run failed due to {}".format(e))
main()

