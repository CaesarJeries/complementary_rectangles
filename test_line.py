import unittest
from rect_comp import (Point,
                       HorizontalLine,
                       VerticalLine,
                       get_intersection,
                       does_intersect,
                       InvalidTangentException)

class TestLine(unittest.TestCase):

    def test_exception(self):
        def create_horizontal_line():
            HorizontalLine(Point(0, 1), Point(42, 42))
        
        def create_vertical_line():
            VerticalLine(Point(0, 1), Point(42, 42))

        self.assertRaises(InvalidTangentException, create_horizontal_line)
        self.assertRaises(InvalidTangentException, create_vertical_line)
    
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
    
    def test_does_intersect(self):
        horizontal = HorizontalLine(Point(0, 5), Point(13, 5))
        vertical = VerticalLine(Point(7, 0), Point(7, 25))
        self.assertTrue(does_intersect(vertical, horizontal))

        horizontal = HorizontalLine(Point(0, 5), Point(13, 5))
        vertical = VerticalLine(Point(42, 0), Point(42, 25))
        self.assertFalse(does_intersect(vertical, horizontal))
