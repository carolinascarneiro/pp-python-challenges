# Anagrams
# Two strings are anagrams if you can make one from the other by rearranging the letters.
# Write a function named is_anagram that takes two strings as its parameters. 
# Your function should return True if the strings are anagrams, and False otherwise.
# For example, the call is_anagram("typhoon", "opython") should return True 
# while the call is_anagram("Alice", "Bob") should return False.

#My naive solution

def palindrome(s):
    anagram_s = []
    i = -1
    for y in s:
            anagram_s.append(s[i])
            i = i - 1
    if anagram_s == list(s):
        return True
    else:
        return False

#Solutions PythonPrinciples

# iterative solution:
# keep chopping off the head and tail of the string,
# and compare the two. If they are not equal, it's
# not a palindrome. Stop when the string gets too short.
def palindrome(string):
    while len(string) > 1:
        head = string[0]
        tail = string[-1]
        string = string[1:-1]
        if head != tail:
            return False
    return True

# # recursive solution: equivalent to the above.
# def palindrome(string):
#     if len(string) < 2:
#         return True
#     return string[0] == string[-1] and palindrome(string[1:-1])

# # smarter solution:
# # check if reversing the string gives the same string.
# def palindrome(string):
#     return string == string[::-1]



