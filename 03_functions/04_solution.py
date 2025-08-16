import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area , circumference

a , b = circle_stats(2)

print("Area : ",a , "circumference : ",b)