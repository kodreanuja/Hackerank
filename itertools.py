import itertools
from typing import Iterator
for i in itertools.count(5, 5):
    if i == 35:
        break
    print(i, end = " ")
print("\n")    
for i in itertools.count(4,  4):
    if i == 40:
        break
    print(i, end = " ")
print("\n")
count = 0
for i in itertools.cycle("AB*"):
    if count > 10:
        break
    print(i, end = "") 
    count += 1

print("\n")

l = ["Anuja", "Kodre", "Anuja", "Kodre", "Anuja", "Kodre "]   
Iterators = itertools.cycle(l)
for i in range(7):
    print(next(Iterators), end = " ") 

print("\n")    

# repeat()
print ("Printing the numbers repeatedly : ") 
print (list(itertools.repeat(25, 4)))

print(list(itertools.repeat("*", 10)))
print(list(itertools.repeat(10, 10)))