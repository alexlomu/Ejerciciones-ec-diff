import latex2sympy2
import flask
from sympy import *

init_printing()
def ej1():
    x = symbols("x")
    y = Function("y")
    CI = {y(3): -1}
    ed = Eq( y(x).diff(),(y(x)*(x**2)-y(x))/(y(x)+1))
    print(dsolve(ed, y(x), ics=CI))


def ej2():
    x = symbols("x")
    y = Function("y")
    ed = Eq( sin(x)*y(x).diff(),y(x)*ln(y(x)))
    print(dsolve(ed, y(x)))

def ej3():
    t = symbols("t")
    y = Function("y")
    ed = Eq( y(t).diff() - y(t)/(t-2),2*(t-2)**2)
    print(dsolve(ed, y(t)))

def ej4():
    t = symbols("t")
    y = Function("y")
    ed = Eq( 2*t*y(t).diff() - y(t),3*t**2)
    print(dsolve(ed, y(t)))

