import cmath

# Solve the quadratic equation ax**2 + bx + c = 0

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c"))

if(a==0):
    print("the equation is not quadratic equation")
else:
    delta = b**2 - 4*a*c
    x1 = (-b - cmath.sqrt(delta))/2*a
    x2 = (-b - cmath.sqrt(delta))/2*a
    print("x1: {}\n x2:{}".format(x1,x2))





