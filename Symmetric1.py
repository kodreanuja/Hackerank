"""Task Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both."""
N, M = map(int, input().split())
arr1, arr2 = list(map(int, input().split()))
a = set(arr1)
a1 = set(arr2)
p = arr1.difference(arr2)
q = arr2.difference(arr1)
r = p.union(q)
r = sorted(list(r))
for i in r:
    print(i)