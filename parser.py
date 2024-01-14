from sympy import Function, dsolve, Derivative, checkodesol
import sympy.abc



def get_eqn():
    pass

def solveode_test(y:str, x):
    y=Function(y)

    result = dsolve(Derivative(y(x),x,x) + 9*y(x), y(x))
    print(result)

if __name__=='__main__':
    x = sympy.abc.x
    solveode_test('g',x)
