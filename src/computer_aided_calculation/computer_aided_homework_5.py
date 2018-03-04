from sympy import *
from sympy.geometry import *

# 1
x, y = symbols('x,y')
simplify((x**2 + x) / (x * sin(y)**2 + x * cos(y)**2))

# 2
limit(1/x * ln(exp(x) + 1), x, -oo)

# 3
solveset(x**2 + 2 > x**3, x, S.Reals) & solveset(sqrt(x+2) > x, x, S.Reals)

# 4
a, b, c, d = symbols('a, b, c, d')
solveset(Eq(a * x**3 + b * x**2 + c*x + d, 0), x)

# 5
diff(sin(x+y) * cos(x*y), x, y).subs(x, -1).subs(y, 2).evalf(1000)
diff(sin(x+y) * cos(x*y), x, y).evalf(1000, subs={x: -1, y: 2})


# 6
plot(3*x**2, diff(3*x**2), (x, 0, 5))

# 7
n = symbols('n')

plot(limit((1 + 1/n)**n*x, n, oo), (n, -1, 1))

# 7
n = symbols('n')
plot(limit((1 + 1 / n) ** (n * x), n, oo), (x, -1, 1))

# 8
integrate(exp(-2*x**2), (x, -oo, oo)).evalf(50)

# 9
plot(integrate(exp((-x)**2), x), (x, -4, 4))

# 10
p1x, p1y, p2x, p2y, p3x, p3y = symbols('p1x, p1y, p2x, p2y, p3x, p3y')
a = Point(p1x, p1y)
b = Point(p2x, p2y)
c = Point(p3x, p3y)
triangle = Triangle(a, b, c)
