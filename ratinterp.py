import sympy as sp
import numpy as np

f = lambda x: (3*x**2 - 2*x + 4)/(x**2 - 1/4) 
points = [(1,f(1)),(2,f(2)),(3,f(3)),(4,f(4)),(5,f(5))]

xlst,ylst = zip(*points)
C = sp.diag(*ylst)
V = sp.Matrix(np.vander(xlst,increasing=True))

M = V**-1 @ C @ V
print("\n")
# Va = CVb 
M = M[::,:3]
#sp.pprint(M)

a0,a1,a2,b0,b1,b2 = sp.symbols("a_0 a_1 a_2 b_0 b_1 b_2")
system = (M,sp.Matrix([a0,a1,a2,sp.S.Zero,sp.S.Zero]))

solns = sp.linsolve(system,[b0,b1,b2,a0,a1,a2]).args[0]
x = sp.Symbol("x")

#sp.pprint(solns)
sp.pprint((solns[3] + solns[4]*x + solns[5]*x**2)/(solns[0] + solns[1]*x + solns[2]*x**2))

#One of them may be 1. Thus, there is a unique representation of a polynomial...? 4????
