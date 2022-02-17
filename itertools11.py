from itertools import product
#this tool compute the cartecian product of two itrables. 
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = (tuple(product(A, B)))
print(" ".join(str(i) for i in C))



