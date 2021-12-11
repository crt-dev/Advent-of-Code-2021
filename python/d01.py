
def readInput():
    retval = []
    file = open(r"..\data\01a.txt")
    for line in file:
        retval.append(int(line))
    return retval

def ex01a() :
    input = [199,200,208,210,200,207,240,269,260,263]
    input = readInput()

    count = 0
    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            count += 1

    print(count)



def ex01b():
    #d = [199,200,208,210,200,207,240,269,260,263]
    d = readInput()
    print('size = {}'.format(len(d)))
    scans_per_cycle = 4
    cycle_footprint = 5
    count = 0
    total_cycles = int(len(d) / scans_per_cycle)
    print("cycle\tscan\ti\tprev\this\tcount")
    previous_scan_value = None
    for cycle in range(0, total_cycles): #cycles
        for scan in range(0, scans_per_cycle): #scans
            i = cycle * scans_per_cycle + scan
            scan_value = 0
            for j in range(3):
                if i + j < len(d):
                    scan_value += d[i+j]
                    max = i+j
            if previous_scan_value is not None and scan_value > previous_scan_value:
                count += 1
            print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format(cycle, scan, i, previous_scan_value, scan_value, count, max))
            previous_scan_value = scan_value

    print("operations complete = {}".format(count))

def main():
    #ex01a()
    ex01b()

main()