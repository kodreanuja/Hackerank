from functools import reduce 
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(reduce(lambda x, y: x + (10 ** (y - 1)), range(1, i + 1))**2) 

# in two line code 
for i in range(1, int(input())+1):
    print((((10**i-1)//9))**2)

# above code will print pallindrome traingel.    
