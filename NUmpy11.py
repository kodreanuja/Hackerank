import numpy 
arr1 = numpy.array([12, 34, 56, 78, 5, 1])
arr1.shape = (3, 2)
print(arr1)

temp = []
for i in range(12):
    temp.append(i)
temp1 = numpy.array(temp) 
print(temp1)   
temp1.shape = (4, 3)
print(temp1)

temp2 = []
names = ["Anu", "Mai", "Mukta", "Pritee", "Pillu", "Jiggi", "jimmy", "jiggu", "chimmi"]
for i in names:
    temp2.append(i)
temp2 = numpy.array(temp2)    
temp2.shape = (3, 3)
print(temp2)

N = int(input())
arr = list(map(int, input().split()))
arr = numpy.array(arr)
arr.shape = (3, 2)
print(arr)
