import stddraw
import random

scale_min = -1.25
scale_max = 1.25
num_points = 1000

stddraw.setXscale(scale_min, scale_max)
stddraw.setYscale(scale_min, scale_max)
stddraw.setPenRadius(0.01)

stddraw.circle(0,0,1)
c=0
for c in range(1000):
    while True:
        x = -1.0 + 2.0*random.random()
        y = -1.0 + 2.0*random.random()
        if x*x + y*y <= 1.0:
            stddraw.point(x, y)
            break
stddraw.show()        

