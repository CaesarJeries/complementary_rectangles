import unittest
from rect_comp import (Point,
                       HorizontalLine,
                       VerticalLine,
                       get_intersection)

class TestLine(unittest.TestCase):

    def test_line_intersect(self):

        horizontal = HorizontalLine(Point(0, 5), Point(13, 5))
        vertical = VerticalLine(Point(7, 0), Point(7, 25))

        p = get_intersection(vertical, horizontal)
        self.assertEqual(p, Point(7, 5))

        # reverse order
        horizontal = HorizontalLine(Point(13, 5), Point(0, 5))
        vertical = VerticalLine(Point(7, 25), Point(7, 0))

        p = get_intersection(vertical, horizontal)
        self.assertEqual(p, Point(7, 5))