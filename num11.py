import numpy 



N = int(input())
A = numpy.array([list(map(int,input().strip().split())) for i in range(N)], int)
B = numpy.array([list(map(int, input().strip().split())) for i in range(N)], int)
print(numpy.dot(A, B))
 