# Function 1 - hello world

def greet():
    return "hello world!"

# Opposite number

def opposite(number): 
    return number * -1

# Return Negativev

def make_negative( number ):
    if number > 0:
        return -number
    else:
        return number
    
# Square(n) Sum

def square_sum(numbers):
    return sum (i ** 2 for i in numbers)

# Find the smallest integer in the array

def find_smallest_int(arr):
    return min (arr)

# Grasshopper - Summation

def summation(num):
    return sum (range (1, num + 1))

# Remove String Spaces

def no_space(x):
    return x.replace(" ", "")

# Counting sheep..

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count