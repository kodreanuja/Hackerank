from itertools import product
A = ["anu", "sonu", "jiggu"]
print("The cartesian product using repeat:")
print(list(product(A, repeat = 2)))

B = [1, 2, 3, 4, 5]
C = [2, 3, 2, 3, 2]
print(tuple(product(B, C)))

print()

X = [1, 2, 3, 4, 5, 6]
Y = [1, 2, 3, 4, 5, 6]
Z = list(tuple(product(X,Y)))
print(Z)

count = 0
for i in Z:
    count +=1
print(count)