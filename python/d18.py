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
        self.register = {}
        nq = []
        char_buffer = ""
        buffer = []
        last_bracket = ""
        for n, c in enumerate(num_str):
            if c == '[' and len(nq) == 0:
                self.root = Node(None, "root")
                nq.append(self.root)
                self.register["root"] = self.root
                last_bracket = "["
            elif c == '[' and len(nq) != 0:
                node = Node(None, self.get_new_id())
                node.parent = nq[-1]
                if len(buffer) == 1:
                    nq[-1].x = buffer[0]
                    nq[-1].y = node
                    buffer = []
                    char_buffer = ""
                elif last_bracket == ']':
                    nq[-1].y = node
                else:
                    nq[-1].x = node
                nq.append(node)
                self.register[self.get_new_id()] = node
                last_bracket = "["
            elif c == ']':
                if len(buffer) == 2:
                    node = nq.pop()
                    node.x = buffer[0]
                    node.y = buffer[1]
                    buffer = []
                    char_buffer = ""
                elif len(buffer) == 1:
                    node = nq.pop()
                    node.y = buffer[0]
                    buffer = []
                    char_buffer = ""
                elif last_bracket == ']':
                    nq.pop()
                last_bracket = "]"
            else:
                char_buffer += c
                if "," in char_buffer:
                    buffer = [int(n) for n in char_buffer.split(",") if n != ""]

        # print("register = ", self.register)
        # print("result = ", self.root)
        # print("connectivity = ", )
        # for key, node in self.register.items():
        #     print("{}: connectivity: {}".format(key, node.connectivity()))

    def add(self, b):
        assert isinstance(b, SnailFishNumber)
        del self.register["root"]
        self.root.id = self.get_new_id()
        b_node = b.root
        b_node.id = self.get_new_id()
        new_root = Node(None, "root")
        new_root.x = self.root
        new_root.y = b_node
        self.root.parent = new_root
        b_node.parent = new_root
        self.root = new_root
        self.register["root"] = new_root
        self.register[new_root.x.id] = new_root.x
        self.register[new_root.y.id] = new_root.y
        self.reduce()

    def reduce(self): #check the logic here
        self.explode()
        x_nodes, y_nodes = self.get_nodes_2_split()
        for node in x_nodes:
            self.split_x(node)
            self.explode()
        for node in y_nodes:
            self.split_y(node)
            self.explode()

    def explode(self):
        node = self.get_node_2_explode()
        while node is not None:
            parent = node.parent
            before = str(self.root)
            if node == parent.x:
                parent.x = 0
            elif node == parent.y:
                parent.y = 0
            self.increase_adjacent(before, str(self.root), node.x, "left") #this is bugged because it doesn't find the exact change position
            self.increase_adjacent(before, str(self.root), node.y, "right")
            node = self.get_node_2_explode()


    def increase_adjacent(self, before, after, value, direction):
        #do this via string as this is pretty difficult to do via binary tree
        change_pos = None
        for n, c in enumerate(after):
            if c != before[n]:
                change_pos = n
                break

        if change_pos is not None:
            dir = 1 if direction == "right" else -1
            # offset = 0 if direction == "left" else 2
            # change_pos += offset

            while 0 < change_pos < len(after) - 1:
                change_pos += dir
                char = after[change_pos]
                isdigit = after[change_pos].isdigit()
                if after[change_pos].isdigit():
                    old_value = int(after[change_pos])
                    assert after[change_pos + dir] in [']', ',', '['] #ie. not a double digit number
                    new_value = str(old_value + value)
                    after = after[:change_pos] + new_value + after[change_pos + 1:]
                    self.create(after)
                    break

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
        n = node.parent
        while n is not None:
            depth += 1
            n = n.parent
        return depth

    def get_node_2_explode(self):
        ids = [(id, self.get_depth(node)) for id, node in self.register.items()]
        nodes = [(node, self.get_depth(node)) for id, node in self.register.items()]
        nodes = [node for node, depth in nodes if depth >= 4 and isinstance(node.x, int) and isinstance(node.y, int)]
        return nodes[0] if len(nodes) >= 1 else None


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