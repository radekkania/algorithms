import math
import cmath

# #1
arg1 = 7 * math.sin(math.pi/2)
arg2 = math.cos(0)/3

result1 = 2 * (math.sqrt(arg1 + arg2))**(1/5) - math.log2(18)
print('#1: ' + str(result1))

# #2
result2 = len(str(math.factorial(30) ** 11))
print('#2: ' + str(result2))

#3
result3 = math.gcd(math.factorial(60), 8 ** 120)
print('#3: ' + str(result3))

#4
result4 = int('2021', 3) * int('10212', 3)
print('#4 decimal: ' + str(result4))

#5
a = math.pi/7
b = math.pi ** 2
c = 3/math.pi

result5 = b * (math.tan(2.1 * a) ** c)/3 * math.e ** b - math.cos(a + c)
print('#5: ' + str(result5))

#6
result6 = cmath.e ** complex(0, 2) + cmath.sqrt(-5)
print('#6: ' + str(result6))
