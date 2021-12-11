exercise = r"..\data\07.txt"
example = r"..\data\07ex.txt"

def get_fuel(crab_locations, position):
    fuel = 0
    for i in crab_locations:
        positions = range(i, position) if (position >= i) else range(position, i)
        for n, j in enumerate(positions):
            fuel += n + 1
    return fuel

def get_fuel2(crab_locations, position):
    fuel = 0
    for i in crab_locations:
        n = abs(i - position)
        fuel += n*(n+1)/2
    return fuel


def solution(input_file):
    input = [int(x) for x in open(input_file).read().strip().split(',')]
    min_fuel = None

    for i in range(0, max(input)):
        fuel = get_fuel2(input, i)
        if min_fuel is None:
            min_fuel = fuel
        else:
            min_fuel = fuel if fuel < min_fuel else min_fuel

    return min_fuel

# input = [16]
# print(get_fuel(input, 5))

print(solution(example))
print(solution(exercise))