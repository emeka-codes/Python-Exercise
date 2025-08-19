import pytest
from pythonsolution1 import solveEquation
#where d > 0
def test_real_roots():
    a,b,c= 2,-5,2
    x1, x2= solveEquation(a,b,c)
    assert abs(x1 + x2 + b/a) < 1e-6

#where d == 0
def test_double_roots():
    a,b,c= 1,-2,1
    x,= solveEquation(a,b,c)
    assert abs(2 * x + b/a) < 1e-6

#where d < 0
def test_complex_roots():
    a,b,c = 1,1,1
    x1,x2= solveEquation(a,b,c)
    assert abs((x1 + x2).real + b/a) < 1e-6



