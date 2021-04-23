# complementary Rectangle Calculator

For a demo on how to use the API, please see `main.py`.  
To run the unit tests, execute `python -m unittest test.py`  

The random test is located in the file `test_random.py`

## Algorithm Outline

The main function that runs the algorithm is `get_complement`.  
It receieves a frame (a Rect object), and a list of inner rectangles (a list of Rect objects).  
For each inner rectangle passed to the `get_complement` function, denoted *inner*, the algorithm  
finds the intersections of the lines that are parallel to *inner*'s sides, with the sides of the frame.  
This yields a group of points, all located on the frame.  
Every two points on opposite sides of the frame form a line. Denote this group of lines as *intersect_lines*.   

Next, the algorithm finds the intersection points of every two lines in the group *intersect_lines*.  
This yields a point grid.  
From this grid, we obtain a group of rectangles.  

Finally, we drop the input inner rectangles from this group, and this yields the complementary rectangle group.  
