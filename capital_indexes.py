def capital_indexes(word):
    capitals = []
    
    for i in word:
        an_uppercase_check = i.isupper()
        if an_uppercase_check == True:
            capitals.append(word.index(i))
        print(capitals)
    return(capitals)

capital_indexes("")