
from itertools import combinations_with_replacement


if __name__=="__main__": 
    S = input().split()
    char = sorted(S[0])
    N = int(S[1])
    for i in combinations_with_replacement(char,N):
        print("".join(i))
