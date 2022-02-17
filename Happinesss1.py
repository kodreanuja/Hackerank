"""There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. 
You like all the integers in set  and dislike all the integers in set . Your initial happiness is.
For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements."""
N, M = map(int, input().split())
arr = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
s = [(i in a) - (i in b) for i in arr]
print(sum(s))