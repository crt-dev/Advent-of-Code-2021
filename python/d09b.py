import numpy

exercise = r"..\data\09.txt"
example = r"..\data\09ex.txt"

def get_low_point(input):
    low_points = []
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
                low_points.append((x, y))
                risk += 1 + current

    print("Risk = ", risk)
    return low_points


def get_basin_map(input):
    size = (len(input), len(input[0]))
    map = numpy.full(size, 0)
    for y, line in enumerate(input):
        for x, v in enumerate(line):
            if v == 9:
                map[y, x] = 1
    return map


def flood_basin(map, x, y):
    if map.item(y, x) == 0:
        map[y, x] = 2
        if x > 0:
            flood_basin(map, x - 1, y)
        if x < map.shape[1] - 1:
            flood_basin(map, x + 1, y)
        if y > 0:
            flood_basin(map, x, y - 1)
        if y < map.shape[0] - 1:
            flood_basin(map, x, y + 1)

def solution(input_file):
    input = []
    for line in open(input_file):
        input.append([int(c) for c in line.strip()])

    low_points = get_low_point(input)
    print(low_points)

    basin_sizes = []
    for low_point in low_points:
        basin_map = get_basin_map(input)
        #print("created = \n", basin_map)
        flood_basin(basin_map, low_point[0], low_point[1])
        #print("flooded = \n", basin_map)
        basin_size = numpy.count_nonzero(basin_map == 2)

        if len(basin_sizes) < 3 and basin_size != 0:
            basin_sizes.append(basin_size)
        elif basin_size != 0:
            min_size = min(basin_sizes)
            if basin_size > min_size:
                basin_sizes.append(basin_size)
                basin_sizes.sort()
                basin_sizes = basin_sizes[1:]

    return numpy.prod(basin_sizes)



#risk = 15
#print(solution(example)) #1134

#risk = 633
print(solution(exercise)) #1050192