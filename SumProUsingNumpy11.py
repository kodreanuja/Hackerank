import numpy 
N, M = map(int, input().split())
arr = numpy.array([input().strip().split() for i in range(M)], int)
p = numpy.sum(arr, axis = 0)
print(p)
print(numpy.prod(p, axis = None ))


P, Q = map(int, input().split())
arr1 = numpy.array([input().strip().split() for i in range(Q)], int)
R = numpy.sum(arr1, axis = 0)
print(R)
R1 = numpy.sum(arr1, axis = 1)
print(R1)
R2 = numpy.sum(arr1, axis = None)
print(R2)
print(numpy.prod(R, axis = 0))
print(numpy.prod(R , axis = 1))
print(numpy.prod(R, axis = None))

print(numpy.max(numpy.min(numpy.array([input().split() for _ in range(int(input().split()[0]))],int),axis=1)))
