#!/usr/bin/env python3

import unittest
from get_frame_compliment import get_compliment, Rect, Point


class GetComplimentTest(unittest.TestCase):

    def test_already_full_single_rect(self):
        frame = Rect(Point(0, 0), Point(42, 42))
        rects = [Rect(Point(0, 0), Point(42, 42))]
        c_rects = get_compliment(frame, rects)
        
        self.assertEqual(len(c_rects), 0)
    
    def test_already_full_multiple_rect_vertical(self):
        frame = Rect(Point(0, 0), Point(42, 42))
        rects = [Rect(Point(0, 0), Point(21, 42)), Rect(Point(21, 0), Point(42, 42))]
        c_rects = get_compliment(frame, rects)
        
        self.assertEqual(len(c_rects), 0)
    
    def test_already_full_multiple_rect_horizontal(self):
        frame = Rect(Point(0, 0), Point(42, 42))
        rects = [Rect(Point(0, 0), Point(42, 21)), Rect(Point(0, 21), Point(42, 42))]
        c_rects = get_compliment(frame, rects)
        
        self.assertEqual(len(c_rects), 0)
    
if __name__ == '__main__':
    unittest.main()
