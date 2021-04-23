from .rect import Rect


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
    if len(rects) == 0:
        return [frame]
    
