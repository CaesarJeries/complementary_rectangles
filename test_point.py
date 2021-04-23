import unittest
import math
from rect_comp import Point

class TestPoint(unittest.TestCase):

    def test_equality(self):
        p = Point(0, 0)
        self.assertEqual(p, p)

        # test with round-off errors
        p = Point(1. / 3, 1. / 3)
        self.assertEqual(p, p)

        p1 = Point(1, 2)
        p2 = Point(52, 2)
        self.assertNotEqual(p1, p2)
        
        p1 = Point(1, 1. / 9)
        p2 = Point(math.pi, 1. / 9)
        self.assertNotEqual(p1, p2)
