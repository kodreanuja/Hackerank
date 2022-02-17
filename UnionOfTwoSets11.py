# union without duplication all elements from both
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
lis = set(a).union(set(b))
print(len(lis))

# intersection the elements that are unique in both the sets.
lis1 = set(a).intersection(set(b))
print(len(lis1))

# difference 
lis2 = set(a).difference(set(b))
print(len(lis2))

# Symmetric_difference 
lis3 = set(a).symmetric_difference(set(b))
print(len(lis3))

# A is the subset of B or Not 
for i in range(int(input())):
    x = input() 
    a = set(input().split())
    z = input() 
    b =set(input().split())
    print(a.issubset(b))

a = set(map(int, input().split()))
print(all([a.issuperset(set(map(int, input().split()))) for i in range(int(input()))]))
