# Challenge

# Consecutive zeros
# The goal of this challenge is to analyze a binary string consisting of only zeros and ones. 
# Your code should find the biggest number of consecutive zeros in the string. 
# For example, given the string:
# "1001101000110"
# The biggest number of consecutive zeros is 3.
# Define a function named consecutive_zeros that takes a single parameter, 
# which is the string of zeros and ones. 
# Your function should return the number described above.

def consecutive_zeros(s):
    zero = []
    a = []
    r = range(0, len(s)-1)
    for i in r:
        if s[i] and s[i+1] == "0":
            a.append(0)
        else:
            a.append("Nop")
    x = a.split("Nop")
    print(x)

consecutive_zeros("1001101000110")