import random
import math

# Area of square: l^2
# Area of circle: pi*r^2 = pi*l^2/4

def generate_pnt():
    # Generates a point in the region {-1<x<1, -1<y<1} and returns whether it's with circle of radius 1 centered at origin
    x = random.random()
    y = random.random()
    return math.sqrt(x**2+y**2) < 1

s = 0
itr = 10**6
for i in range(itr):
    s += generate_pnt()
print(4*s/itr)