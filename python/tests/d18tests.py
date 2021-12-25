import unittest
from ..d18 import *

class d18tests(unittest.TestCase):

    def check_magnitude(self, input, magnitude):
        snum = SnailFishNumber(input)
        self.assertEqual(input, str(snum.root))
        self.assertEqual(magnitude, snum.root.magnitude())

    def check_addition(self, input, expected_snum, expected_magnitude):
        snum = add_list(input)
        self.assertEqual(expected_snum, str(snum))
        self.assertEqual(expected_magnitude, snum.magnitude())

    def check_explode(self, input, expected):
        snum = SnailFishNumber(input)
        snum.explode()
        self.assertEqual(expected, str(snum.root))


    def test_12(self):
        self.check_magnitude("[1,2]", 7)

    def test_double_digit_input_supported(self):
        self.check_magnitude("[10,10]", 50)

    def test_123_a(self):
        self.check_magnitude("[[1,2],3]", 27)

    def test_123_b(self):
        self.check_magnitude("[1,[2,3]]", 27)

    def test_1234_a(self):
        input = "[1,[2,[3,4]]]"
        self.check_magnitude(input, 83)

    def test_1234_b(self):
        input = "[[[1,2],3],4]"
        self.check_magnitude(input, 89)

    def test_1234_c(self):
        input = "[1,[[2,3],4]]"
        self.check_magnitude(input, 91)

    def test_magnitude_a(self):
        input = "[[1,2],[[3,4],5]]"
        self.check_magnitude(input, 143)

    def test_magnitude_b(self):
        input = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
        self.check_magnitude(input, 1384)

    def test_magnitude_c(self):
        input = "[[[[1,1],[2,2]],[3,3]],[4,4]]"
        self.check_magnitude(input, 445)

    def test_magnitude_d(self):
        input = "[[[[3,0],[5,3]],[4,4]],[5,5]]"
        self.check_magnitude(input, 791)

    def test_magnitude_e(self):
        input = "[[[[5,0],[7,4]],[5,5]],[6,6]]"
        self.check_magnitude(input, 1137)

    def test_magnitude_f(self):
        input = "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
        self.check_magnitude(input, 3488)

    def test_add_1234(self):
        input = ["[1,1]", "[2,2]", "[3,3]", "[4,4]"]
        expected = "[[[[1,1],[2,2]],[3,3]],[4,4]]"
        self.check_addition(input, expected, 445)

    def not_a_test_get_depth(self):
        input = "[[[[1,1],[2,2]],[3,3]],[4,4]]"
        snum = SnailFishNumber(input)
        self.assertEqual(input, str(snum.root))
        for id, node in snum.register.items():
            print(id, " depth = ", snum.get_depth(node))
        explode_list = [node for id, node in snum.register.items() if snum.get_depth(node) >= 4]
        print("explode_list = ", explode_list)

    def test_split_y(self):
        input = "[5,9]"
        snum = SnailFishNumber(input)
        snum.root.y = 11
        snum.split_y(snum.root)
        self.assertEqual(snum.root.y.x, 5)
        self.assertEqual(snum.root.y.y, 6)

    def test_split_x(self):
        input = "[0,0]"
        snum = SnailFishNumber(input)
        snum.root.x = 13
        snum.split_x(snum.root)
        self.assertEqual(snum.root.x.x, 6)
        self.assertEqual(snum.root.x.y, 7)

    def test_explode_1(self):
        input = "[[[[[9,8],1],2],3],4]"
        expected = "[[[[0,9],2],3],4]"
        self.check_explode(input, expected)

    def test_explode_2(self):
        input    = "[7,[6,[5,[4,[3,2]]]]]"
        expected = "[7,[6,[5,[7,0]]]]"
        self.check_explode(input, expected)

    def test_explode_3(self):
        input = "[[6,[5,[4,[3,2]]]],1]"
        expected = "[[6,[5,[7,0]]],3]"
        self.check_explode(input, expected)

    def test_explode_4(self):
        input    = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
        expected = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
        self.check_explode(input, expected)

    def test_explode_5(self):
        input = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
        expected = "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
        self.check_explode(input, expected)

    def test_add_12345(self):
        input = ["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]"]
        expected = "[[[[3,0],[5,3]],[4,4]],[5,5]]"
        self.check_addition(input, expected, 791)

    def test_add_123456(self):
        input = ["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]", "[6,6]"]
        expected = "[[[[5,0],[7,4]],[5,5]],[6,6]]"
        self.check_addition(input, expected, 1137)

    def test_increase_adjacent_right(self):
        before = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
        after  = "[[3,[2,[8,0]]],[6,[5,[4,[3,2]]]]]"
        expected = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
        snum = SnailFishNumber(before)
        snum.increase_adjacent(before, after, 3, "right")
        self.assertEqual(expected, str(snum))

    def test_increase_adjacent_right_double_digit(self):
        before = "[[3,[2,[1,[7,5]]]],[6,[5,[4,[3,2]]]]]"
        after  = "[[3,[2,[8,0]]],[6,[5,[4,[3,2]]]]]"
        expected = "[[3,[2,[8,0]]],[11,[5,[4,[3,2]]]]]"
        snum = SnailFishNumber(before)
        snum.increase_adjacent(before, after, 5, "right")
        self.assertEqual(expected, str(snum))

