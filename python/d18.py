from collections import Counter, defaultdict
import numpy as np
from pprint import pprint
from math import floor, ceil

day = "18"
exercise_file = r"..\data\d{0}.txt".format(day)
example_file = r"..\data\d{0}eg.txt".format(day)

def get_input(input_file):
    input = [x.strip() for x in open(input_file)]
    return input

def solution(input):
    answer = input[0]
    return answer

class Node:
    def __init__(self, parent, id):
        self.parent = parent
        self.id = id
        self.x = self.y = None

    def items(self):
        assert self.x is not None and self.y is not None
        return [self.x, self.y]

    def magnitude(self):
        value_x = self.x if isinstance(self.x, int) else self.x.magnitude()
        value_y = self.y if isinstance(self.y, int) else self.y.magnitude()
        return 3 * value_x + 2 * value_y

    def __repr__(self):
        return "[{},{}]".format(self.x, self.y)

    def connectivity(self):
        cx = "{}".format(self.x.id) if isinstance(self.x, Node) else str(self.x)
        cy = "{}".format(self.y.id) if isinstance(self.y, Node) else str(self.y)
        return "[{},{}]".format(cx, cy)


class SnailFishNumber:
    def __init__(self, input):
        self.root = None
        self.register = {}
        self.id = 0
        self.create(input)

    def __repr__(self):
        return str(self.root)

    def magnitude(self):
        return self.root.magnitude()

    def get_new_id(self):
        self.id += 1
        return "N" + str(self.id)

    def create(self, num_str):
        num_str = num_str.replace(',', '')
        nq = []
        buffer = []

        for n, c in enumerate(num_str):
            if c == '[' and len(nq) == 0:
                self.root = Node(None, "root")
                nq.append(self.root)
                self.register["root"] = self.root
            elif c == '[' and len(nq) != 0:
                node = Node(None, self.get_new_id())
                node.parent = nq[-1]
                if len(buffer) == 1:
                    nq[-1].x = buffer[0]
                    nq[-1].y = node
                    buffer = []
                elif num_str[n-1] == ']':
                    nq[-1].y = node
                else:
                    nq[-1].x = node

                nq.append(node)
                self.register[self.get_new_id()] = node
            elif c == ']':
                if len(buffer) == 2:
                    node = nq.pop()
                    node.x = buffer[0]
                    node.y = buffer[1]
                    buffer = []
                elif len(buffer) == 1:
                    node = nq.pop()
                    node.y = buffer[0]
                    buffer = []
                elif num_str[n-1] == ']':
                    node = nq.pop()

            elif c != ',':
                buffer.append(int(c))

        print("register = ", self.register)
        print("result = ", self.root)
        print("connectivity = ", )
        for key, node in self.register.items():
            print("{}: connectivity: {}".format(key, node.connectivity()))

    def add(self, b):
        assert isinstance(b, SnailFishNumber)
        del self.register["root"]
        self.root.id = self.get_new_id()
        b_node = b.root
        b_node.id = self.get_new_id()
        new_root = Node(None, "root")
        new_root.x = self.root
        new_root.y = b_node
        self.root = new_root
        self.register["root"] = new_root
        self.register[new_root.x.id] = new_root.x
        self.register[new_root.y.id] = new_root.y
        self.reduce()

    def reduce(self): #check the logic here
        self.explode_all()
        x_nodes, y_nodes = self.get_nodes_2_split()
        for node in x_nodes:
            self.split_x(node)
            self.explode()
        for node in y_nodes:
            self.split_y(node)
            self.explode()

    def explode_all(self): #untested
        nodes_2_explode = self.get_nodes_2_explode()
        while (len(nodes_2_explode) != 0):
            for node in nodes_2_explode:
                self.explode(node)

    def explode(self, node):
        parent = node.parent
        if node == parent.x:
            parent.y += node.y
            parent.x = 0
            while parent is not None:
                parent = parent.parent
                if parent is not None and isinstance(parent.x, int):
                    parent.x += node.x
                    break
        elif node == parent.y:
            parent.x += node.x
            parent.y = 0
            while parent is not None:
                parent = parent.parent
                if isinstance(parent.y, int):
                    parent.y += node.y
                    break
                if parent is None: #we're at root and havn't found the right most
                    child



    def split_x(self, node):
        assert isinstance(node.x, int)
        new_node = Node(node, self.get_new_id())
        new_node.x = floor(node.x/2)
        new_node.y = ceil(node.x/2)
        node.x = new_node
        self.register[new_node.id] = new_node

    def split_y(self, node):
        assert isinstance(node.y, int)
        new_node = Node(node, self.get_new_id())
        new_node.x = floor(node.y/2)
        new_node.y = ceil(node.y/2)
        node.y = new_node
        self.register[new_node.id] = new_node

    def get_depth(self, node):
        depth = 0
        n = node
        while n is not None:
            depth += 1
            n = n.parent
        return depth

    def get_nodes_2_explode(self):
        return [node for id, node in self.register.items() if self.get_depth(node) >= 5]

    def get_nodes_2_split(self):
        x_nodes = [node for id, node in self.register.items() if isinstance(node.x, int) and node.x > 9]
        y_nodes = [node for id, node in self.register.items() if isinstance(node.y, int) and node.x > 9]
        return x_nodes, y_nodes



def add_list(input):
    snum = SnailFishNumber(input[0])
    for item in input[1:]:
        b = SnailFishNumber(item)
        snum.add(b)
    return snum



#example_input = get_input(example_file)
#exercise_input = get_input(exercise_file)

#[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
#print(solution(example_input)) #4140
#print(solution(exercise_input)) #

# try:
#     read_snail_number2("[[1,2],3]")
#     #read_snail_number2("[1,[2,3]]")
#     #read_snail_number2("[1,[2,[3,4]]]")
#     #read_snail_number2("[[[1,2],3],4]")
# except Exception as e:
#     print(e)
# #read_snail_number2("[[1,2],3]")