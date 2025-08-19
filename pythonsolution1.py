import math 
import cmath
def solveEquation(a, b, c):
    if a == 0:
        raise ValueError("'a' cannot be zero")
    
    d= pow(b,2) - 4 * a * c

    if d > 0:
        x1, x2 = (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)
        print (f'x1 = {x1:.1f}, x2 = {x2:.1f}')
        return x1, x2
    
    elif d < 0:
        x1, x2 = (-b + cmath.sqrt(d)) / (2 * a), (-b - cmath.sqrt(d)) / (2 * a)
        print (f'x1 = {x1:.1f}, x2 = {x2:.1f}')
        return x1, x2

    elif d == 0:
        x= (-b + cmath.sqrt(d)) / (2 * a)
        print(f'x = {x}')
        return (x,)


    
