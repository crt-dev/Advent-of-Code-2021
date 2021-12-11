import copy

def process(line):
    line_elements = line.split()
    return line_elements[0], int(line_elements[1])


def read_input(file_name):
    data = []
    file = open(r"..\data\{0}.txt".format(file_name))
    for line in file:
        data.append(line.strip())
    return data


def q1(file_name):
    data = read_input(file_name)
    gamma = ""
    epsilon = ""
    for i in range(0, len(data[0])):
        count0 = 0
        count1 = 0
        for j in range(0, len(data)):
            if data[j][i] == "1":
                count1 += 1
            else:
                count0 += 1
        if count1 > count0:
            gamma += "1"
            epsilon += "0"
        elif count0 > count1:
            gamma += "0"
            epsilon += "1"
        else:
            raise Exception("equal counts!")

    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)
    power_consumption = gamma_decimal * epsilon_decimal
    return power_consumption

def get_digit(count1, count0, reading_type):
    reading = str()
    if count1 >= count0:
        if reading_type == "oxygen":
            reading += "1"
        else:
            reading += "0"
    elif count0 > count1:
        if reading_type == "oxygen":
            reading += "0"
        else:
            reading += "1"
    return reading

def get_reading(data, reading_type):
    reading_size = len(data[0])
    reading = ""

    for i in range(0, reading_size):
        count0 = 0
        count1 = 0
        for j in range(0, len(data)):
            if data[j][i] == "1":
                count1 += 1
            else:
                count0 += 1
        reading += get_digit(count1, count0, reading_type)

        data_filter = filter(lambda o: o.startswith(reading), data)
        data = list(data_filter)

        if len(data) == 0:
            raise Exception("Something is wrong as filtered list is empty")

        if len(data) == 1:
            return data[0]

    raise Exception("Something is wrong as didn't find anything")


def q2(file_name):
    data = read_input(file_name)
    oxygen_reading = get_reading(copy.deepcopy(data), "oxygen")
    c02_reading = get_reading(copy.deepcopy(data), "c02")
    oxygen_generator_decimal = int(oxygen_reading, 2)
    c02_scrubber_decimal = int(c02_reading, 2)
    life_support = oxygen_generator_decimal * c02_scrubber_decimal
    return life_support


def q2_old(file_name):
    data = read_input(file_name)
    oxygen_data = copy.deepcopy(data)
    c02_data = copy.deepcopy(data)
    oxygen_generator = ""
    c02_scrubber = ""
    oxygen_generator_found = None
    c02_scrubber_found = None

    for i in range(0, len(data[0])):
        count0 = 0
        count1 = 0
        for j in range(0, len(data)):
            if data[j][i] == "1":
                count1 += 1
            else:
                count0 += 1
        if count1 >= count0:
            oxygen_generator += "1"
            c02_scrubber += "0"
        elif count0 > count1:
            oxygen_generator += "0"
            c02_scrubber += "1"
        # else:
        #     oxygen_generator += "1"
        #     c02_scrubber += "0"

        if oxygen_generator_found is None:
            oxygen_filter = filter(lambda o: o.startswith(oxygen_generator), oxygen_data)
            oxygen_data = list(oxygen_filter)

        if c02_scrubber_found is None:
            c02_filter = filter(lambda o: o.startswith(c02_scrubber), c02_data)
            c02_data = list(c02_filter)

        if len(oxygen_data) == 0 or len(c02_data) == 0:
            raise Exception("Something is wrong as filtered lists are empty")

        if oxygen_generator_found is None and len(oxygen_data) == 1:
            oxygen_generator_found = oxygen_data[0]
        if c02_scrubber_found is None and len(c02_data) == 1:
            c02_scrubber_found = c02_data[0]

    if oxygen_generator_found is None or c02_scrubber_found is None:
        raise Exception("Not all values found")


    oxygen_generator_decimal = int(oxygen_generator_found, 2)
    c02_scrubber_decimal = int(c02_scrubber_found, 2)
    life_support = oxygen_generator_decimal * c02_scrubber_decimal
    return life_support


def run():
    exercise = "03"
    example = "{}ex".format(exercise)
    q1_ex_expected = 198
    q2_ex_expected = 230
    ans_q1ex = q1(example)
    ans_q1 = q1(exercise)
    ans_q2ex = q2(example)
    ans_q2 = q2(exercise)

    #correct
    #4139586
    #1800151

    print("*" * 100)
    print("\tq1ex = {0} {1}\n\tq1 = {2}\n\tq2ex = {3} {4}\n\tq2 = {5}".format(
        ans_q1ex, "EXPECTED" if ans_q1ex == q1_ex_expected else "WRONG", ans_q1,
        ans_q2ex, "EXPECTED" if ans_q2ex == q2_ex_expected else "WRONG", ans_q2))
    print("*" * 100)


def main():
    try:
        run()
    except Exception as e:
        print("Run failed due to {}".format(e))


main()
