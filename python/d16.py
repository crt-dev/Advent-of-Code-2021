from collections import Counter, defaultdict, deque
import numpy as np
from pprint import pprint
import functools
import operator

day = "16"
exercise_file = r"..\data\{0}.txt".format(day)
example_file = r"..\data\{0}ex.txt".format(day)

hex2bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

L_TYPE_FIXED = 0
L_TYPE_NUM = 1


def get_input(input_file):
    input = open(input_file).read().strip()
    return input

class MessageQueue:
    def __init__(self, hex=None):
        self.q = deque()
        if hex is not None:
            self.create_from_hex(hex)

    def create_from_hex(self, hex): # str = bin(int(c, 16))[2:]
        for c in hex:
            bin = hex2bin[c]
            for b in bin:
                self.q.append(b)

    def create_from_binary(bin):
        message_queue = MessageQueue()
        for c in bin:
            message_queue.q.append(c)
        return message_queue

    def n_pop(self, n):
        retval = ""
        for n in range(n):
            retval += self.q.popleft()
        return retval

    def get_version(self):
        return int(self.n_pop(3), 2)

    def get_type(self):
        return int(self.n_pop(3), 2)

    def get_element(self):
        return int(self.n_pop(3), 2)

    def get_length_type(self):
        length_type = int(self.n_pop(1), 2)
        if length_type == L_TYPE_FIXED:
            length_value = int(self.n_pop(15), 2)
        elif length_type == L_TYPE_NUM:
            length_value = int(self.n_pop(11), 2)
        return length_type, length_value

    def get_literal(self, has_eom): #only discard when we're expecting an end of message
        length = 6
        binary = ""
        while True:
            element = self.n_pop(5)
            binary += element[1:]
            length += 5
            if element[0] == '0':
                break
        if has_eom:
            self.discard_eom(length)

        return int(binary, 2)

    def discard_eom(self, length):
        if length % 4 != 0: #discard trailing zeros
            discard_length = 0
            while (length + discard_length) % 4 != 0:
                discard_length += 1
            discard = self.n_pop(discard_length)
            assert discard.count('0') == discard_length

    def assert_empty(self):
        assert(len(self.q) == 0)


class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.literal = None
        self.sub_packets = []

    def value(self):
        """
        TYPE_SUM = 0
        TYPE_PRODUCT = 1
        TYPE_MIN = 2
        TYPE_MAX = 3
        TYPE_GREATER = 5
        TYPE_LESS = 6
        TYPE_EQUAL = 7

        """
        value = None
        values = [p.value() for p in self.sub_packets]
        match self.type:
            case 0:
                value = sum(values)
            case 1:
                value = functools.reduce(operator.mul, values)
            case 2:
                value = min(values)
            case 3:
                value = max(values)
            case 5: #greater than
                assert(len(values) == 2)
                value = 1 if values[0] > values[1] else 0
            case 6: #less than
                assert(len(values) == 2)
                value = 1 if values[0] < values[1] else 0
            case 7: #equal
                assert(len(values) == 2)
                value = 1 if values[0] == values[1] else 0
        return value


class PacketLiteral(Packet):
    def __init__(self, version, type, literal):
        self.version = version
        self.type = type
        self.literal = literal
        self.sub_packets = []

    def value(self):
        return self.literal


class PacketOperator(Packet):
    def __init__(self, version, type, length_type, sp_length, sub_packets):
        self.version = version
        self.type = type
        self.length_type = length_type
        self.sp_length = sp_length
        self.sub_packets = sub_packets
        self.literal = None

class PacketFactory:
    def __init__(self, q):
        self.mq = q

    def create_from_hex(hex_input):
        message_queue = MessageQueue(hex_input)
        return PacketFactory(message_queue)

    def create_from_binary(binary_input):
        q = MessageQueue.create_from_binary(binary_input)
        return PacketFactory(q)

    def create_packets(self, has_eom=True):
        packets = []
        while self.mq.q:
            packet = self.create_packet(has_eom)
            packets.append(packet)
        return packets

    def create_n_packets(self, n):
        packets = []
        while len(packets) < n:
            packet = self.create_packet(False)
            packets.append(packet)
        assert len(packets) == n
        return packets

    def create_packet(self, has_eom=True):
        version = self.mq.get_version()
        type = self.mq.get_type()
        message_length = 6
        if type == 4:  #literal
            literal = self.mq.get_literal(has_eom)
            return PacketLiteral(version, type, literal)
        else: #operator
            length_type, length_value = self.mq.get_length_type()
            if length_type == L_TYPE_FIXED:
                sub_packet_binary = self.mq.n_pop(length_value)
                packet_factory = PacketFactory.create_from_binary(sub_packet_binary)
                sub_packets = packet_factory.create_packets(False)
                message_length += length_value
                if has_eom:
                    self.mq.discard_eom(message_length)
            elif length_type == L_TYPE_NUM:
                sub_packets = self.create_n_packets(length_value)

            return PacketOperator(version, type, length_type, length_value, sub_packets)

    def get_version_sum(self, hex_input): pass

    def get_value(self, hex_input): pass

def get_version_sum(packet):
    version_sum = packet.version
    for p in packet.sub_packets:
        version_sum += get_version_sum(p)
    return version_sum

def get_value_sum(packet):
    value_sum = packet.value()
    for p in packet.sub_packets:
        value_sum += get_value_sum(p)
    return value_sum

def sum_version(packets):
    version_sum = 0
    for p in packets:
        version_sum += get_version_sum(p)
    return version_sum

def sum_values(packets):
    value_sum = 0
    for p in packets:
        value_sum += get_value_sum(p)
    return value_sum

def solution_p1():
    hex_input = get_input(exercise_file)
    packet_factory = PacketFactory.create_from_hex(hex_input)
    packets = packet_factory.create_packet()
    return sum_version([packets])

def solution_p2():
    hex_input = get_input(exercise_file)
    return get_value(hex_input)

def get_value(hex_input):
    packet_factory = PacketFactory.create_from_hex(hex_input)
    packet = packet_factory.create_packet()
    return packet.value()


#print(solution_p1()) #901
print(solution_p2()) #
# print(solution(exercise_file)) #
