def word_count(s):
    # Your code here
    ignore_characters = ('"', "'", ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "?")
    chaching = {}
    
    for i in ignore_characters:
        s = s.replace(i, "$$")
        
    s = s.lower().split()
    for word in s:
        if word in chaching:
            chaching[word] += 1
        else:
            chaching[word] = 1
    return chaching   




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))