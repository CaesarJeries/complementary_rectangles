
class Point(object):
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


class Rect(object):

    def __init__(self, p1, p2):
        self.bottom_left = p1
        self.top_right = p2


def get_compliment(frame, rects):
    """
    frame - an axis-aligned rectangle (R)
    rects - a list of smaller rectangles which satisfy the following conditions:
                - axis-aligned
                - bound by `frame`
                - non-overlapping
    
    @return a list of complimentary non-overlapping rectangles, denoted c_rects, such that
            the union of `rects` and c_rects covers the entirety of `frame`
    """
    pass
