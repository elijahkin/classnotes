import math

def rate_of_change_equation(x, y):
    return (math.e)**(-(x/5)**2)

def eulers_method(inital_condition, step_size, max_x):
    x, y = float(inital_condition[0]), float(inital_condition[1])
    while x <= max_x + 0.1:
        slope = rate_of_change_equation(x, y)
        print('%.03f %.07f %.03f' % (x, y, slope))
        x += step_size
        y += slope * step_size

eulers_method((0, 0), 0.1, 2)