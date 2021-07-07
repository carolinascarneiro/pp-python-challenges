# Counting syllables
# Define a function named count that takes a single parameter. 
# The parameter is a string. 
# The string will contain a single word divided into syllables by hyphens, such as these:
# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"
# Your function should count the number of syllables and return it.
# For example, the call count("ho-tel") should return 2.

#My naive method

def count(word):
    n = 0
    for i in list(word):
        if i == "-":
            n += 1
    return n+1

count("met-a-phor")

# # naive solution
# def count(word):
#     syllables = 1
#     for letter in word:
#         if letter == "-":
#             syllables = syllables + 1
#     return syllables

# # using the count method
# def count(word):
#     return word.count("-") + 1

# # using split
# def count(word):
#     return len(word.split("-"))