# Type check
# Write a function named only_ints that takes two parameters. 
# Your function should return True if both parameters are integers, and False otherwise.
# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.


#My naive method
def only_ints(a, b):
    c = 1
    type_check = type(a) == type(c) and type(b) == type(c)
    if type_check == True:
        return True
    else: 
        return False

#Method Python Principles


    

only_ints("b", 2)
