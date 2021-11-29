def greet(name):
    print("Hello, " + name + ". How are you?")



def countWords(): 
    intro=input("Introduce yourself: ")
    words=0
    wordlist=intro.split()
    print(wordlist) 
    words=words+len(wordlist)
    print(words)
    

countWords()