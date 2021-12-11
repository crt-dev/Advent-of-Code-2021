exercise = r"..\data\09.txt"
example = r"..\data\09ex.txt"


def solution(input_file):
    input = []
    for line in open(input_file):
        input.append([int(c) for c in line.strip()])

    low_points = 0
    risk = 0

    y_max = len(input)
    for y, Y in enumerate(input):
        x_max = len(Y)
        for x, X in enumerate(Y):
            adj = []
            if x == 0:
                if y == 0: #top left corner
                    adj = [(x + 1, y), (x, y + 1)]
                elif y == y_max - 1: #bottom left
                    adj = [(x + 1, y), (x, y - 1)]
                else:
                    adj = [(x, y - 1), (x + 1, y), (x, y + 1)] #left side
            elif x == x_max - 1:
                if y == 0: #top right
                    adj = [(x - 1, y), (x, y + 1)]
                elif y == y_max - 1: #bottom right
                    adj = [(x, y - 1), (x -1, y)]
                else:
                    adj = [(x, y - 1), (x -1, y), (x, y + 1)] #right side
            else:
                if y == 0: #top side
                    adj = [(x - 1, y), (x, y + 1), (x + 1, y)]
                elif y == y_max - 1: #bottom side
                    adj = [(x - 1, y), (x, y - 1), (x + 1, y)]
                else:
                    adj = [(x, y - 1), (x, y + 1),  (x - 1, y), (x + 1, y)]

            low_count = 0
            current = input[y][x]
            for a in adj:
                comparison = input[a[1]][a[0]]
                if current < comparison:
                    low_count += 1

            if low_count == len(adj):
                print("found low point ", current)
                low_points += 1
                risk += 1 + current



    return risk


print(solution(example)) #15
print(solution(exercise)) #633