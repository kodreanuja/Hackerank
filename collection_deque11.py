from collections import deque
n = int(input())
d = deque()
for i in range(n):
    method, *args  = input().split(maxsplit=1)
    getattr(d, method)(*args)
[print(x, end=' ') for x in d]