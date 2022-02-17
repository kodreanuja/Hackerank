N = int(input())
for i in range(1, N+1):
    for j in range(1, i+1):
        print(i, end="")
    print()    

print("\n")

Size = int(input())
for i in range(1, Size):
    for j in range(1, i+1):
        print(i, end = "")
    print() 

print("\n")

# within two line it will print N-1 numerical traingle.
size1 = int(input())   
for i in range(1, size1):
    print(int(i* 10 ** i/9) ) 