import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( 1/((sy.sqrt(x))*(1 + x)), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[1,1,1,1,0,0,0,0,0,0], [0,0,0,0,1,1,1,1,-1,0], 
                   [-2/3,0,0,0,1,0,0,0,0,0], [0,-3/4,0,0,0,1,0,0,0,0],
                   [0,0,-1/3,0,0,0,1,0,0,0], [0,0,0,-4/5,0,0,0,1,0,0],
                   [0,0,0,0,-1,3,0,0,0,0], [0,0,0,0,0,0,-1,235/136,0,0],
                   [-1,-1,1/25,1/25,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,1]] )
    b = np.array([1820,0,0,0,0,0,0,0,0,100])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 10905186 # my id is 0905186
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
