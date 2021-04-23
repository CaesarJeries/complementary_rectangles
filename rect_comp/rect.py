from .point import Point


class Rect(object):

    def __init__(self, p1: Point, p2: Point):
        """
        p1 - the bottom left corner of the rectangle
        p2 - the top right corner of the rectangle
        """
        self.bottom_left = p1
        self.top_right = p2
    
    def __eq__(self, other):
        return self.bottom_left == other.bottom_left and \
               self.top_right == other.top_right
    
