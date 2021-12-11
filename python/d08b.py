from collections import Counter, defaultdict

exercise = r"..\data\08.txt"
example = r"..\data\08ex2.txt"

digit_map = {}
# digit_map["".join(sorted("acedgfb"))] = 0
# digit_map["".join(sorted("acedgfb"))] = 0
# digit_map["".join(sorted("acedgfb"))] = 0
# digit_map["".join(sorted("acedgfb"))] = 0
# digit_map["".join(sorted("acedgfb"))] = 0
# digit_map["".join(sorted("acedgfb"))] = 0
# digit_map["".join(sorted("acedgfb"))] = 0
# digit_map["".join(sorted("acedgfb"))] = 0
# digit_map["".join(sorted("acedgfb"))] = 0

digit_map["abcdef"] = 0
digit_map["bc"] = 1
digit_map["abdeg"] = 2
digit_map["abcdg"] = 3
digit_map["bcfg"] = 4
digit_map["acdfg"] = 5
digit_map["acdefg"] = 6
digit_map["abc"] = 7
digit_map["abcdefg"] = 8
digit_map["abcdfg"] = 9


# digit_map["".join(sorted("acedgfb"))] = 8
# digit_map["".join(sorted("cdfbe"))] = 5
# digit_map["".join(sorted("gcdfa"))] = 2
# digit_map["".join(sorted("fbcad"))] = 3
# digit_map["".join(sorted("dab"))] = 7
# digit_map["".join(sorted("cefabd"))] = 9
# digit_map["".join(sorted("cdfgeb"))] = 6
# digit_map["".join(sorted("eafb"))] = 4
# digit_map["".join(sorted("cagedb"))] = 0
# digit_map["".join(sorted("ab"))] = 1

length_map = { 2:1, 4:4, 3:7, 7:8}

def read_input(input_file):
    input = []
    for line in open(input_file):
        elements = line.strip().split('|')
        definitions = elements[0].split()
        digits = elements[1].split()
        input.append((definitions, digits))
    return input

def get_value(digit):
    counter = Counter(c for c in digit)
    count = len(counter)
    if count in length_map:
        lookup = length_map[len(digit)]
        return str(lookup)
    elif count == 6: #either 6,9,0
        return "0"
    elif count == 5: #either 2,3,5
        return "0"
    else:
        raise Exception("Unexpected digit")

def interpret_definition(definitions):
    definitions = sorted(definitions, key=len)
    interpretation = {}

    #pass 1
    for definition in definitions:
        sdef = "".join(sorted(definition))
        if len(sdef) == 2:
            one = set(sdef)
            interpretation[sdef] = 1
        elif len(sdef) == 3:
            seven = set(sdef)
            interpretation[sdef] = 7
        elif len(sdef) == 4:
            four = set(sdef)
            interpretation[sdef] = 4
        elif len(sdef) == 7:
            interpretation[sdef] = 8

    #pass 0,6,9
    for sdef in ["".join(sorted(x)) for x in definitions if len(x) == 6]:
        one_diff = one.difference(set(sdef))
        four_diff = four.difference(set(sdef))
        if len(one_diff) == 1:
            interpretation[sdef] = 6
        elif len(four_diff) == 1:
            interpretation[sdef] = 0
        else:
            interpretation[sdef] = 9

    #pass 2,3,5
    for sdef in ["".join(sorted(x)) for x in definitions if len(x) == 5]:
        one_diff = one.difference(set(sdef))
        four_diff = four.difference(set(sdef))
        if len(one_diff) == 0:
            interpretation[sdef] = 3
        elif (len(four_diff)) == 2:
            interpretation[sdef] = 2
        elif (len(four_diff)) == 1:
            interpretation[sdef] = 5
        else:
            raise Exception("interpretation 2,3,5 assumption not valid")

    assert len(interpretation) == 10
    return interpretation



def solution(input_file):
    input = read_input(input_file)

    sum = 0
    for line in input:
        definitions = line[0]
        interpretation = interpret_definition(definitions)
        number = ""
        for digit in line[1]:
            sdigit = "".join(sorted(digit))
            number += str(interpretation[sdigit])
        line_num = int(number)
        #print(number)
        sum += line_num

    print("\n-------\n")
    return sum

#print(solution(example))
print(solution(exercise))