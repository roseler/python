import random

#For Number 1

points = 1000000
points_in_circle = 0

for i in range(points):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        points_in_circle += 1

print("Pi is approximately", 4 * points_in_circle / points)


#For Number 2

num_points = 100000
points_under_curve = 0

p1 = (-1, 2)
p2 = (2, -2)

for i in range(num_points):
    x = random.uniform(p1[0], p2[0])
    y = random.uniform(p1[1], p2[1])
    if y <= x**2 and x >= p1[0] and x <= p2[0]:
        points_under_curve += 1
        
area = points_under_curve / num_points * (p2[0] - p1[0]) * (p2[1] - p1[1])

print("Area is approximately", area)

#For Number 3

pointss = 100000
points_inside_ellipsoid = 0

a, b, c = 2, 3, 4

for i in range(pointss):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)
    z = random.uniform(-c, c)
    if x*x/a + y*y/b + z*z/c <= 1:
        points_inside_ellipsoid += 1
    
volume = points_inside_ellipsoid / pointss * 8 * a * b * c

print("Volume is approximately", volume)
