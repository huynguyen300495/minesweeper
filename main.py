from screen import get_screenshot
from cursor import *
from solver import Solver
from squareImage import *
import time
from cursor import *

left_click(6,4)
time.sleep(1)

while True:

	image_path = get_screenshot()
	matrix = get_matrix(image_path)

	for row in matrix:
	    print(' '.join([str(x) for x in row]))

	solver = Solver()
	solver.update_matrix(matrix)
	
	safeSquares = solver.get_safe_squares()

	for x,y in safeSquares:
		left_click(x,y)
		time.sleep(0.5)


