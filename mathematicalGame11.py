N1 = int(input())
N2 = int(input())                         
print(N1//N2)                           #17
print(N1%N2)                             #7
print(divmod(N1, N2))                   #  (17, 7)

N = int(input())
N3 = int(input())
N4 = int(input())

print(N**N3) 
print(pow(N, N3))

print(pow(N, N3, N4))
print(N1 ** N3 % N4)

# 
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b + c**d)            