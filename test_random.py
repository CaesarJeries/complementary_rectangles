import numpy as np
import logging
import unittest
import sys
from rect_comp import Rect, Point, get_compliment

def generate_random_inner_rects(num_rects, frame):
    x_iter = frame.bottom_left.x
    x_end = frame.top_right.x
    y_iter = frame.bottom_left.y
    y_end = frame.top_right.y

    rects = []
    while x_iter < x_end and y_iter < y_end and num_rects > 0:
        arr = np.random.random_sample(2) 
        bottom_left = Point(x_iter, y_iter)
        x = arr[0] * (x_end - x_iter) + x_iter
        y = arr[1] * (y_end - y_iter) + y_iter
        top_right = Point(x, y)
        r = Rect(bottom_left, top_right)
        rects.append(r)
        num_rects -= 1
        x_iter += x
        y_iter += y
    
    return rects


def gen_random_frame():
    max_value = 2**16
    arr = np.random.random_sample(4) * max_value
    arr = sorted(arr)
    p = Point(arr[0], arr[1])
    return Rect(p, Point(p.x + arr[2], p.y + arr[3]))


class TestRandom(unittest.TestCase):
    def test_random(self):
        for _ in range(100):
            num_inners = np.random.randint(100)
            frame = gen_random_frame()
            rects = generate_random_inner_rects(num_inners, frame)
            comp_rects = get_compliment(frame, rects)
            total_area = frame.area()
            area_sum = sum(r.area() for r in comp_rects)
            area_sum += sum(r.area() for r in rects)

            self.assertAlmostEqual(total_area, area_sum, places=4)
