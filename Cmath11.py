import cmath
number = complex(input())
print(*cmath.polar(number), sep = "\n")


# how to print the angle between two sides of the traingle.
import math
AB = int(input())
BC = int(input())
H = math.sqrt(AB**2 + BC**2)
H = H/2.0
adj = BC/ 2.0
O = math.degrees((math.acos(adj/H)))
O = round(O)
O = str(O)
print(O + chr(176))

size1 = int(input())
size2 = int(input())
a = int(round(math.degrees(math.atan(size1,size2))))
print(a, chr(176))