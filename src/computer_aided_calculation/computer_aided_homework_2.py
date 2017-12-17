from fractions import Fraction as Frac
from decimal import Decimal as Dec
from decimal import getcontext
import math as m

# 1
print('#1 - a 2.5% tax on a $1.40 charge (rounded to the nearest cent')

result1_1 = round(Dec('1.025') * Dec('1.40'), 2)
result1_2 = round(float('1.025') * float('1.40'), 2)

print('decimal ' + str(result1_1))
print('float ' + str(result1_2))
print('\n')

# 2
print('#2 remainder after division of 10.5 by 0.2')
result2 = Dec(10.5) % Dec(0.2)

print(result2)
print('\n')

# 3
print('#3 500 significant decimal figures of Euler’s constant')
getcontext().prec = 500
result3 = Dec(1).exp()
print(result3)
print('\n')

# 4
print('#4')
result4 = Frac('2.5') * Frac(3, 5) + (1+Frac(1, 10)) * (9+Frac(2, 17)) - Frac('7.81')
print(result4)

# 5
print('#5')
a = Frac('1.1')
b = Frac(-1, 2)
c = 3+Frac(2, 21)

result5 = c * (a + b) + a*b - 2*c + Frac(a, c)
print(result5)
print('\n')

# 6
print('#6')

e = Dec(1).exp()
result6 = Frac(e).limit_denominator(19)

print('\n')

# 7
print('#7')
a = Frac(int('232', 5), int('211', 3))
b = Frac(int('5463', 8), int('325', 6))

result7 = a - b
print(result7)
