#!/usr/bin/env python3

from rect_comp import Point, Rect, get_intersection, get_compliment, get_intersect_points

# a demonstation of the API

frame = Rect(Point(0, 0), Point(100, 100))
r1 = Rect(Point(13, 13), Point(20, 25))
r2 = Rect(Point(27, 17), Point(45, 42))
r3 = Rect(Point(32, 50), Point(63, 70))

crects = get_compliment(frame, [r1, r2, r3])

print('The complimentary rectangle set (each represented by its botton left and top right corners:')
for r in crects:
    print(r)
