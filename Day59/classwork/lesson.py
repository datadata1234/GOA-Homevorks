# Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    x = 0
    y = 0
    
    for i in arr:
        if i > 0:
            x += 1
        else:
            y += i
            
    return [x,y]

# Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
# Simple multiplication

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    
# Invert values

def invert(lst):
    result = []
    
    for i in lst:
        result.append(-i)
    
    return result

# Beginner - Reduce but Grow

def grow(arr):
    st = 1
    for i in arr:
        st = st * i 
    return st
        
# Disemvowel Trolls

def disemvowel(string_):
    aeiou = "aeiou"
    for i in aeiou:
        string_ = string_.replace(i, "")
        string_ = string_.replace(i.upper(),"")
    return string_

# Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted(numbers)[0] + sorted(numbers)[1]
