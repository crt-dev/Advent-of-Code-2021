from collections import Counter

file_01a = r"..\..\data\01a.txt"
file_02 = r"..\..\data\02.txt"
file_05 = r"..\..\data\05.txt"
file_06 = r"..\..\data\06.txt"

#read list of string
input1 = [x.strip() for x in open(file_01a)]

#read list of int
input1b = [int(x) for x in open(file_01a)]

#read list of delmited strings
input2 = [x for x in open(file_02)]

#read single line csv integers into list
input3 = [int(x) for x in open(file_06).read().strip().split(',')]

#read int list with multiple delimiters
input5 = [[int(y) for y in x.strip().replace(' -> ', ',').split(',')] for x in open(file_05)]

#read list into dictionary
input6 = Counter([int(x) for x in open(file_06).read().strip().split(',')])

print('done')