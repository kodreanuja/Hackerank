import numpy 
N, M = map(int, input().split())
a, b = (numpy.array([input().split() for i in range(N)], dtype=int) for i in range(2))
print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(a // b)
print(numpy.mod(a, b))
print(numpy.power(a, b))


numpy.set_printoptions(legacy = '1.13')

arr= list(map(float, input().split()))
arr = numpy.array(arr)
arr1 = numpy.floor(arr)
print(arr1)
arr2 = numpy.ceil(arr)
print(arr2)
arr3 = numpy.rint(arr)
print(arr3)


# sum and product by using numpy.
N, M = map(int, input().split())
arr = numpy.array([input().strip().split() for i in range(M)], int)
print(numpy.sum(arr, axis = 0))
print(numpy.sum(arr, axis = 1))
print(numpy.sum (arr, axis = None))
print(numpy.prod(arr, axis = 1))
print(numpy.prod(arr, axis = 0 ))
print(numpy.prod(arr, axis = None))