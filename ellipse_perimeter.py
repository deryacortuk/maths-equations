from math import pi
def ellipse(a,b):
    if(a>0 and b>0):
        perimeter = 2*pi*(0.5*(a**2 + b**2))**0.5
        return perimeter
    else:
        return False
def ellipse_area(a,b):
    if(a>0 and b>0):
        area=(pi*a*b)/4
        return  area
    else:
        return False
print(ellipse_area(3,4))
print(ellipse(3,4))