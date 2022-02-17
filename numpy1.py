import numpy 
arr = list(map(int, input().split()))
arr = numpy.ones(arr, dtype = numpy.int)
print(arr)
arr1 = list(map(int, input().split()))
arr1 = numpy.ones(arr1, dtype = numpy.int)
print(arr1)


# numpy identity 
arr2 = numpy.identity(3)
print(arr2)

arr4 = numpy.identity(2)
print(arr4)

# numpy eye
N, M = map(int, input().split())
arr = numpy.eye(N, M)
print(arr)

arr1 = numpy.eye(3, 3)
print(arr1)

# numpy.set for perfect alignment.
numpy.set_printoptions(legacy = '1.13')
N, M = map(int, input().split())
arr = numpy.eye(N, M)
print(arr)

