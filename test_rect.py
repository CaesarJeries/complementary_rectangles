import unittest
from rect_comp import Point, Rect

class TestRect(unittest.TestCase):

    def test_overlap(self):
        r1 = Rect(Point(0, 0), Point(13, 13))
        r2 = Rect(Point(13, 13), Point(20, 25))

        self.assertFalse(r1.does_overlap(r2))

        r3 = Rect(Point(13.00, 17.00), Point(20.00, 25.00))

        self.assertTrue(r2.does_overlap(r3))
        self.assertTrue(r3.does_overlap(r2))