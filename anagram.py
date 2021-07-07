
def anagrams(a, b):
    newlist = []
    for i in b:
        if i in a:
            newlist.append("Yes")
        else: 
            newlist.append("No")

    if "No" in newlist:
        print(False)
    else:
        print(True)
        
anagrams("test", "tess")