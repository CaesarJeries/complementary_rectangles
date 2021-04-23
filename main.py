#!/usr/bin/env python3

from rect_comp import Point, Rect, get_intersection

frame = Rect(Point(0, 0), Point(100, 100))
r = Rect(Point(13, 13), Point(42, 42))

lines = r.get_intersect_lines(frame)

print('Top line')
print(lines['top'])

print('Bottom line')
print(lines['bottom'])

print('Left line')
print(lines['left'])

print('Right line')
print(lines['right'])

frame_lines = frame.get_frame_lines()

horizontal_lines = [frame_lines['top'], frame_lines['bottom'], lines['top'], lines['bottom']]
vertical_lines = [frame_lines['left'], frame_lines['right'], lines['left'], lines['right']]

intersect_points = []
for h in horizontal_lines:
    for v in vertical_lines:
        intersect_points.append(get_intersection(v, h))

for p in intersect_points:
    print(p)
