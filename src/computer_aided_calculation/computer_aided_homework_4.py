import random as rand
import statistics as st
from math import fsum
from functools import reduce
import math
from fractions import Fraction as F

N = 40
L = list(rand.uniform(0, 9) for i in range(40))
print(L)

# 1 arithmetic mean
l_mean = st.mean(L)

try:
    l_mode = st.mode(L)
except st.StatisticsError as e:
    print('error occurred: only unique values: ' + str(e))

l_median = st.median(L)


# 2
result2 = any((x**2 >= 2) and (x**2 < 5) for x in L)
print(result2)


# 3
print('#3')
print(L)
reduce(lambda x, y: (x*2**5*x)*y, L)

reduce(lambda x, y: x*y, (x*2**5*x for x in L)) - min(v-4+3*math.sin(v) if v > 5 else v**2 + 5 * math.cos(v)**3 for v in L)

# 4
print(L)
max1 = max((elem-8 for x, elem in enumerate(L)), key=abs)


# 4 proper solution
max2 = max(L, key=lambda x: abs(x-8))
print("max2: " + str(max2))

# 5
result5 = max(i * e - i for i, e in enumerate(L))
print(result5)

# 6
sum1 = fsum(a/b for a in L for b in (2, 3, 8, 9) if a**2 > b)

# 7
list_i = {x for x in range(9)}


# 8






