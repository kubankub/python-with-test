import unittest
import math

class TestMy(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math.add(2, 3), 5)

    def test_add2(self):
        self.assertEqual(math.add(0, -1), -1)

#    def test_sum(self):
#        self.assertEqual(math.sum(2, 3, 4), 6)

