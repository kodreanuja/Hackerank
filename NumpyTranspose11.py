import numpy
arr = [[1, 2, 3], [3, 4, 5]]
arr = numpy.array(arr)
arr1 = numpy.transpose(arr)
print(arr1)
arr1 = arr1.flatten()
print(arr1)

#concate two array in numpy
M, N, P = map(int, input().split())
arr1 = numpy.array([input().strip().split() for i in range(M)], int)
arr2 = numpy.array([input.strip().split() for i in range(N)], int)
arr3 = numpy.concatenate(arr1, arr2, axis = 0)
print(arr3)

# zero tool in numpy 
arr = numpy.zeros((1, 2))
print(arr)
arr1 = numpy.zeros((1, 2), dtype = numpy.int)
print(arr1)