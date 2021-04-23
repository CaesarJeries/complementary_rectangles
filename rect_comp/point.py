import sys

class Point(object):
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other):
        eps = sys.float_info.epsilon
        return abs(self.x - other.x) < eps and abs(self.y - other.y) < eps
    
    def __str__(self):
        return '({:.2f}, {:.2f})'.format(self.x, self.y)
