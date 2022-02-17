"""Let's dive into decorators! You are given mobile numbers. Sort them in ascending order then print them in 
the standard format shown below: The given mobile numbers may have ,  or  written before the actual  digit number.
Alternatively, there may not be any prefix at all."""

def wrapper(f):
    def fun(l):

        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])

    return fun

@wrapper                                # decorator 
def sort_phone(l):
    print(*sorted(l), sep='\n')         # sort into the order.

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

