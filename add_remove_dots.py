# Adding and removing dots
# Write a function named add_dots that takes a string and adds "." in between each letter. 
# For example, calling add_dots("test") should return the string "t.e.s.t".
# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. 
# For example, calling remove_dots("t.e.s.t") should return "test".
# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string 
# for any string.
# (You may assume that the input to add_dots does not itself contain any dots.)

#My naive solution
import re

def add_dots(text):
    text_1 = list(text)
    x = range(0,len(text))
    for i in x:
        text_1.insert(i+i, ".")
    text_1.pop(0)
    text = "".join(text_1)
    return text

def remove_dots(text):
    text = text.replace(".", "")
    return text

remove_dots(add_dots("test"))

# # the longer way
# def add_dots(s):
#     out = ""
#     for letter in s:
#         out += letter + "."
#     return out[:-1]

# def remove_dots(s):
#     out = ""
#     for letter in s:
#         if letter != ".":
#             out += letter
#     return out


# # the short way
# def add_dots(s):
#     return ".".join(s)

# def remove_dots(s):
#     return s.replace(".", "")

