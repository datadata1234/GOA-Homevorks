# List Filtering

def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result

# Jaden Casing Strings

def to_jaden_case(string):
    result = []
    string = string.split()
    for i in string:
        result.append(i.capitalize())
    return " ".join(result)

# Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted(numbers)[0] + sorted(numbers)[1]

# Is this a triangle?

# NO

# Two to One

def longest(a1, a2):
    result = set(a1 + a2)
    list1 = "".join(sorted(result)) 
    return list1


