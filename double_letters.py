# Double letters
# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
# For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical 
# letters in a row. Define a function named double_letters that takes a single parameter. 
# The parameter is a string. Your function must return True if there are two identical letters in a row in the string,
# and False otherwise.

#My naive solution
def double_letters(word):
    digit_check = 0
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            digit_check = digit_check + 1
    if digit_check == 0:
        return False
    else:
        return True

#Solution from Python Principles

# naive solution
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False

# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])



double_letters("Carrol")