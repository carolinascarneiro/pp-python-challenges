# Challenge

# Middle letter
# Write a function named mid that takes a string as its parameter.
# Your function should extract and return the middle letter.
# If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

#My naive solution

def mid(word):
    # retornando string com index do meio encontrado 
    return word[(int(len(word)/2))] if (len(word)-(int(len(word)/2)*2) != 0) else ""
print(mid("aloa"))



# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
# def mid(string):
#     if len(string) % 2 == 0:
#         return ""
#     return string[len(string)//2]



