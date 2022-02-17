import operator
import time 
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# we can calculate the time .
t1 = time.time()
a, b, c = map(operator.mul, A, B)
t2 = time.time()
print(a, b, c)
print("Time taken by map function : %6f "%(t2 - t1))

# use map for addition.
x = list(map(operator.add, A, B))
print(x)

# use map for substraction 
Y = list(map(operator.sub, A, B))
print(Y)

# use map for mod 
Z = list(map(operator.abs, A))
print(Z)

# navie mathod 
t3 = time.time()
for i in range(3):
    print(A[i] * B[i], end = " ")
t4 = time.time()
print("\n time taken  for navie method :%6f" %(t3 - t4))


# naive for substrction
l = len(A)
for i in range(l):
    print(A[i] - B[i], end = "")

print("\n")

# naive for addition 
for i in range(l):
    print(A[i] + B[i], end = " ")



