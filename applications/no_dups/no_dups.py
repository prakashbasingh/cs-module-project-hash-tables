def no_dups(s):
    # Your code here
    no_dups = {}
    new_string = ""
    s = s.split()
    
    for word in s:
        if word not in no_dups:
            no_dups[word] = True
            new_string += word + " "
    
    return new_string.strip()
        


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))