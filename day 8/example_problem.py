'''you are painting a wall. the instruction on the paint can says that 1 can of paint can cover 5 square meters of wall.
given a random height and width of wall, calculate how many cans of paint you will need to buy'''


import math

def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print (f"You will need {number_of_cans} cans of paint")

test_h = int(input("Height of wall : "))
test_w = int(input("Width of wall : "))
coverage = 5
paint_calc(test_h, test_w, coverage)