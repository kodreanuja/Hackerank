def convertOppositeCase(s):
    l = len(s)
    for i in range(l):
        if s[i] >= "a" and s[i] <= "z":
            s[i] = chr(ord(s[i]) - 32)
        
        elif s[i] >= "A" and s[i] <= "Z":
            s[i] = chr(ord(s[i])+32) 
    s= ''.join(s) 
    return s        


if __name__ == "__main__":
    s = input() 
    s = list(s) 
    print(convertOppositeCase(s))  