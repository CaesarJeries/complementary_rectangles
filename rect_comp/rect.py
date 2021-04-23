from .point import Point
from .line import HorizontalLine, VerticalLine


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
    
    def get_corners(self):
        return [
            self.bottom_left,
            Point(self.bottom_left.x, self.top_right.y), # top left
            self.top_right,
            Point(self.top_right.x, self.bottom_left.y) # bottom right
        ]
    
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
    