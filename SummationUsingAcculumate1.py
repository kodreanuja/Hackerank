import itertools 
lis = list(map(int, input().split()))
print(list(itertools.accumulate(lis, lambda x, y : x + y )))
""" acculumate is used for ading previous to the next and print the sum of it  """

print("\n")
# 1+ 3 = 4; 4+ 4 = 8; 8+ 10 = 10; 18 + 4 = 22
li = [1, 3, 4, 10, 4]
sum = 0
temp = []
for i in range(len(li)):
    sum += li[i]
    temp.append(sum)
print(temp)
    



    
