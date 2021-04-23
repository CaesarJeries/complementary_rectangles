import sys

class Point(object):
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other):
        eps = sys.float_info.epsilon
        return abs(self.x - other.x) < eps and abs(self.y - other.y) < eps
    
    def __lt__(self, other):
        # test for equality since data member are floats
        if self == other:
            return False

        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        elif self.y < other.y:
            return True
        
        return False
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __str__(self):
        return '({:.2f}, {:.2f})'.format(self.x, self.y)
