# Jaden Casing Strings

def to_jaden_case(string):
    result = []
    string = string.split()
    for i in string:
        result.append(i.capitalize())
    return " ".join(result)

# Sum of a sequence

def sequence_sum(begin_number, end_number, step):
    result = 0
    for i in range(begin_number, end_number + 1, step):
        result += i 
    return result

# egex count lowercase letters

def lowercase_count(strng):
    re = 0
    for i in strng:
        if i.islower():
            re += 1 
            
    
    return re