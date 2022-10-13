import latex2sympy2
import flask
from sympy import *

init_printing()

def ej1():
    x = symbols("x")
    y = Function("y")
    CI = {y(3): -1}
    ed = Eq( y(x).diff(),(y(x)*(x**2)-y(x))/(y(x)+1))
    dsolve(ed, y(x), ics=CI)

