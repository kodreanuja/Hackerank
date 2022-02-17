def mutate_string(string, position, character):
    a = string[:position] + character + string[position+1:]
    
    
    return a

if __name__ == '__main__':
    string = input()
    positon, character = input().split()
    s_new = mutate_string(string, int(positon), character)
    print(s_new)