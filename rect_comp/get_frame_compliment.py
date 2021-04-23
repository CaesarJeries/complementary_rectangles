import itertools
import logging

from .point import Point
from .rect import Rect
from .line import get_intersection

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def get_vertical_lines(rects):
    rects_lines = [r.get_frame_lines() for r in rects]
    vertical_lines = [[e['left'], e['right']] for e in rects_lines]
    vertical_lines = list(itertools.chain.from_iterable(vertical_lines)) # flatten list
    return vertical_lines


def get_horizontal_lines(rects):
    rects_lines = [r.get_frame_lines() for r in rects]
    horizontal_lines = [[e['top'], e['bottom']] for e in rects_lines]
    horizontal_lines = list(itertools.chain.from_iterable(horizontal_lines)) # flatten list
    return horizontal_lines


def get_intersect_points(frame, rects):
    all_rects = rects[:]
    all_rects.append(frame)
    vlines = get_vertical_lines(all_rects)
    hlines = get_horizontal_lines(all_rects)

    intersection_points = []
    for v in vlines:
        for h in hlines:
            p = get_intersection(v, h)
            intersection_points.append(p)
    
    # return unique values 
    return list(set(intersection_points))


def create_rects_from_points(intersection_points):
    """
    `intersection_points` are sorted using the default comparison operator of Point
    """
    grid = []
    for _, group in itertools.groupby(intersection_points, lambda p: p.x):
        grid.append(list(group))
    
    for l in grid:
        for p in l:
            print(p, end=' ')
        print()
    
    rects = []
    for i in range(len(grid) - 1):
        for j in range(len(grid[i]) - 1):
            bottom_left = Point(grid[i][j].x, grid[i][j].y)
            top_right = Point(grid[i+1][j+1].x, grid[i+1][j+1].y)
            r = Rect(bottom_left, top_right)
            rects.append(r)
    
    return rects


def remove_overlapping_rects(comp_rects, input_rects):
    def does_overlap(current, group):
        for r in group:
            if r.does_overlap(current):
                return True
        return False
    
    retval = []
    for r in comp_rects:
        if does_overlap(r, input_rects):
            continue
        retval.append(r)
    
    return retval


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
    
    intersection_points = get_intersect_points(frame, rects)
    intersection_points.sort()

    all_rects = create_rects_from_points(intersection_points)
    comp_rects = all_rects[:]
    for r in comp_rects:
        # remove input rectangle
        if r in rects:
            comp_rects.remove(r)

    print('before remove', len(comp_rects))
    for r in comp_rects:
        print(r)

    comp_rects = remove_overlapping_rects(comp_rects, rects) 
    
    print('Total rects:', len(comp_rects))
    for r in comp_rects:
        print(r)

    return comp_rects 
