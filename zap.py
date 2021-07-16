# Custom zip
# The built-in zip function "zips" two lists. Write your own implementation of this function.
# Define a function named zap. The function takes two parameters, a and b. These are lists.
# Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
# You may assume a and b have equal lengths.
# If you don't get it, think of a zipper.

def zap(a, b):
    return [(a[y], b[y]) for y in range(0, len(a))]
    #old solution
    # c = []
    # for y in range(0, len(a)):
    #     c.append((a[y], b[y]))
    # print(c)

#Python Principle Solutions
# # ugly but understandable solution
# def zap(a, b):
#     result = []
#     for i in range(len(a)):
#         item_from_a = a[i]
#         item_from_b = b[i]
#         tup = (item_from_a, item_from_b)
#         result.append(tup)
#     return result

# # concise solution with list comprehensions
# def zap(a, b):
#     return [(a[i], b[i]) for i in range(len(a))]