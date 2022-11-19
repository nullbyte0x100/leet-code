def count(sentence):

    vowel=['a','e','i','o','u']
    
    return len([i for i in sentence if i in vowel])
if __name__=="__main__":
    print(count("jake malesi"))

