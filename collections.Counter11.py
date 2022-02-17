import collections

X = int(input())
lis = collections.Counter(map(int, input().split()))
N = int(input())
    

income = 0

for i in range(N):
    size, price = map(int, input().split())
    if lis[size]: 
        income += price
        lis[size] -= 1

print (income)
