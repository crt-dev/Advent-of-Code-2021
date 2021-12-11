from collections import defaultdict, Counter

#mylist = [int(x) for x in open(file_06).read().strip().split(',')]
#read list into dictionary
#mydict = Counter([int(x) for x in open(file_06).read().strip().split(',')])

import re

def other():
    #1:04
    input01 = open("01.txt").read()

    #1:05 but incorrect
    input05 = [x.strip() for x in open("05.txt")]

    #6:04 split on multiple characters (better way to do this but involves regex)
    input06 = [x.strip().replace(' ', ',').split(',') for x in open("06.txt")]


    print("wau")


input09 = [x.strip().replace(' to ', ' = ').split(' = ') for x in open("input.txt")]

print('done')