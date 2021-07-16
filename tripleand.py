# Challenge

# Boolean and
# Define a function named triple_and that takes three parameters and returns True 
# only if they are all True and False otherwise.

def triple_and(a, b, c):
    print(len([i for i in [a, b, c] if i != True]) == 0)
        
#Python Principle Solutions

# def triple_and(a, b, c):
#     return a and b and c I missed it because I tried return a, b, c. 
# Didn't know it could be used in a different way!