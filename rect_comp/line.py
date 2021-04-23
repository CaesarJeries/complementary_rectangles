import sys
import logging
from .point import Point

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

class VerticalLine(object):
    def __init__(self, p1, p2):
        eps = sys.float_info.epsilon
        if abs(p1.x - p2.x) > eps:
            raise Exception('Invalid tangent. The line must be vertical')
        
        yt = max(p1.y, p2.y)
        yb = min(p1.y, p2.y)
        logging.debug('Created a vertical line with yt, yb = {:.2f}, {:.2f}'.format(yt, yb)) 
        self.top = Point(p1.x, yt)
        self.bottom = Point(p1.x, yb)


class HorizontalLine(object):
    def __init__(self, p1, p2):
        eps = sys.float_info.epsilon
        if abs(p1.y - p2.y) > eps:
            raise Exception('Invalid tangent. The line must be horizontal')

        x_right = max(p1.x, p2.x)
        x_left = min(p1.x, p2.x)
        logging.debug('Created a horizontal line with x_left, x_right = {:.2f}, {:.2f}'.format(x_left, x_right)) 
        self.left = Point(x_left, p1.y)
        self.right = Point(x_right, p1.y)


def get_intersection(vertical: VerticalLine, horizontal: HorizontalLine):
    return Point(vertical.top.x, horizontal.left.y)
