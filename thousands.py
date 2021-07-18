# Thousands separator
# Write a function named format_number that takes a non-negative number as its only parameter.

# Your function should convert the number to a string and add commas as a thousands separator.

# For example, calling format_number(1000000) should return "1,000,000".

def format_number(n):
    l = str(n).split()
    print(l, type(l))
    i = -1
    for item in l:
        print("Hi")
        l[i-2] = "," + l[i-2]
        i -= 1
        print(l)
    

format_number(1000000)
    print(str(f"{n:,}"))