import math
def quadratic(a, b, c):
    if not (isinstance(a,(int, float)) and isinstance(b,(int, float)) and isinstance(c,(int, float))):
       raise TypeError('bad operand type')
    if b*b-4*a*c < 0:
        print('no answer')
        return None
    d = math.sqrt(b*b-4*a*c)
    x1 = (-b-d)/2/a
    x2 = (-b+d)/2/a
    return x1,x2
