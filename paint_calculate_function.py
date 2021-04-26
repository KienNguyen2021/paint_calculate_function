import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_can = math.ceil(area / cover)

    print (f" You will need {num_of_can}")




test_h = int(input(" Height of the wall : "))
test_w = int(input(" Width of the wall : "))
coverage = 5

paint_calc(height = test_h, width = test_w, cover = coverage)
