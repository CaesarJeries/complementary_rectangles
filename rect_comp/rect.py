import logging
import sys

from .point import Point
from .line import HorizontalLine, VerticalLine, does_intersect

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

class Rect(object):

    def __init__(self, p1: Point, p2: Point):
        """
        p1 - the bottom left corner of the rectangle
        p2 - the top right corner of the rectangle
        """
        self.bottom_left = p1
        self.top_right = p2

    def __str__(self):
        return 'Bottom left: {}, Top right: {}'.format(self.bottom_left, self.top_right)
    
    def __eq__(self, other):
        return self.bottom_left == other.bottom_left and \
               self.top_right == other.top_right
    
    def get_corners(self):
        return {
            'bottom_left': self.bottom_left,
            'top_left': Point(self.bottom_left.x, self.top_right.y), # top left
            'top_right': self.top_right,
            'bottom_right': Point(self.top_right.x, self.bottom_left.y) # bottom right
        }
    
    def get_frame_lines(self):
        top_line = HorizontalLine(Point(self.bottom_left.x, self.top_right.y), Point(self.top_right.x, self.top_right.y))
        bottom_line = HorizontalLine(Point(self.bottom_left.x, self.bottom_left.y), Point(self.top_right.x, self.bottom_left.y))
        right_line = VerticalLine(Point(self.top_right.x, self.bottom_left.y), Point(self.top_right.x, self.top_right.y))
        left_line = VerticalLine(Point(self.bottom_left.x, self.bottom_left.y), Point(self.bottom_left.x, self.top_right.y))

        return {
            'top': top_line,
            'bottom': bottom_line,
            'right': right_line,
            'left': left_line
        }
    
    def is_point_inside(self, p: Point):
        return self.bottom_left.x < p.x < self.top_right.x and \
               self.bottom_left.y < p.y < self.top_right.y
    
    def does_overlap(self, other):
        logging.debug('Self: {}\t|\tOther: {}'.format(self, other))
        def lte(p1, p2):
            eps = sys.float_info.epsilon
            if abs(p1 - p2) < eps:
                return True
            return p1 < p2
        
        if  lte(self.top_right.x, other.bottom_left.x) or \
            lte(other.top_right.x, self.bottom_left.x):
                return False
        
        if  lte(self.top_right.y, other.bottom_left.y) or \
            lte(other.top_right.y, self.bottom_left.y):
                return False

        logging.debug('Overlap detected: {} | {}'.format(self, other)) 
        return True

    def get_intersect_lines(self, frame):
        """
        frame - a rectangle that contains self

        Returns 4 lines that are the extensions of each side of `self`, where each line is represented by
        2 points on the frmae of the rectangle `frame`.
        Example:
        
            (0, 7)             (7, 7)
            ====X=====Y========
            |                  |
            |   (1, 3)  (5,3)  |
            Z    ______        Z
            |   |     |        |
            W   |_____|        W
            |   (1, 2)  (5, 2) |
            |===X=====Y========|
            (0, 0)              (7, 0)

            The function returns the 4 lines marked X-X / Y-Y / Z-Z / W-W
            where, for example, W-W is the line represented by the following points: (0, 2), (7, 2)
            X-X is (1, 0), (1, 7)

            Z-Z is (0, 3), (7, 3)
        """
        top_line = HorizontalLine(Point(frame.bottom_left.x, self.top_right.y), Point(frame.top_right.x, self.top_right.y))
        bottom_line = HorizontalLine(Point(frame.bottom_left.x, self.bottom_left.y), Point(frame.top_right.x, self.bottom_left.y))
        right_line = VerticalLine(Point(self.top_right.x, frame.bottom_left.y), Point(self.top_right.x, frame.top_right.y))
        left_line = VerticalLine(Point(self.bottom_left.x, frame.bottom_left.y), Point(self.bottom_left.x, frame.top_right.y))

        return {
            'top': top_line,
            'bottom': bottom_line,
            'right': right_line,
            'left': left_line
        }

    def area(self):
        return (self.top_right.x - self.bottom_left.x) * (self.top_right.y - self.bottom_left.y)
