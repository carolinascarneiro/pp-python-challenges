# Challenge

# Capital indexes
# Write a function named capital_indexes. 
#The function takes a single parameter, which is a string. 
#Your function should return a list of all the indexes in
#the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should
# return the list [0, 2, 4].

def capital_indexes(word):
    cap_index = []
    for i in word:
        if i.isupper():
            cap_index.append(word.index(i))
    print(cap_index)

capital_indexes('HeLlO')

#     # naive solution
# def capital_indexes(s):
#     upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result = []
#     for i, l in enumerate(s):
#         if l in upper:
#             result.append(i)
#     return result

# # shorter version
# from string import uppercase
# def capital_indexes(s):
#     return [i for i in range(len(s)) if s[i] in uppercase]

# you can also use the .isupper() string method.