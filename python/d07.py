exercise = r"..\data\07.txt"
example = r"..\data\07ex.txt"

def get_fuel(crab_locations, position):
    fuel = 0
    for i in crab_locations:
        fuel += abs(i - position)
    return fuel


def solution(input_file):
    input = [int(x) for x in open(input_file).read().strip().split(',')]
    min_fuel = None
    for i in input:
        fuel = get_fuel(input,i)
        if min_fuel is None:
            min_fuel = fuel
        else:
            min_fuel = fuel if fuel < min_fuel else min_fuel

    return min_fuel



print(solution(example))
print(solution(exercise))