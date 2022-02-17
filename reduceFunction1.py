from functools import reduce
from fractions import gcd
import math
print(reduce(lambda x, y : x + y, [1, 2, 3, 4]))
print(reduce(lambda a, b : a * b, [1, 2, 3, 2], 4))
print(reduce(lambda p, q : p * q, [3, 4, 5],2))
print(reduce(lambda m, n : m + n , [2, 4, 6], -3))
#print(reduce(gcd, [2, 4, 8], 3))
reduce(math.gcd, [2,4,8], 3)

from fractions import Fraction 
import operator 
def product(fracs):
    t = reduce(operator.mul, fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)