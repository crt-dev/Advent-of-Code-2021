import unittest

from ..d06 import q1, q2

class base_test(unittest.TestCase):
    def setUp(self):
        self.exercise = "06"
        self.example = "{}ex".format(self.exercise)

class q1_test(base_test):

    def test_q1_example_18(self):
        answer = q1(self.example, 18)
        self.assertEqual(answer, 26)

    def test_q1_example_80(self):
        answer = q1(self.example, 80)
        self.assertEqual(answer, 5934)

    def test_q1(self):
        answer = q1(self.exercise, 80)
        self.assertEqual(answer, 380758)


class q2_test(base_test):

    def test_q2_example_18(self):
        answer = q2(self.example, 18)
        self.assertEqual(answer, 26)

    def test_q1_example_80(self):
        answer = q2(self.example, 80)
        self.assertEqual(answer, 5934)

    def test_q2_example_256(self):
        answer = q2(self.example, 256)
        self.assertEqual(answer, 26984457539)

    def test_q2_q1(self):
        answer = q1(self.exercise, 80)
        self.assertEqual(answer, 380758)

    def test_q2(self):
        answer = q2(self.exercise, 256)
        self.assertEqual(answer, 1710623015163)