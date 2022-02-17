def is_pallindrome(String):
    rev = ""
    rev = String[::-1]
    if String == rev:
        return True 
    elif String != rev:
        return False
    else:
        return 0   

if __name__ == "__main__":
    String = input()
    print(is_pallindrome(String))    