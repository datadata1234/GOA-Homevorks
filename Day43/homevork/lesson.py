# Sum of a sequence

def sequence_sum(begin_number, end_number, step):
    result = 0
    for i in range(begin_number, end_number + 1, step):
        result += i 
    return result


# List Filtering

# NO


#Jaden Casing Strings

def to_jaden_case(string):
    result = []
    string = string.split()
    for i in string:
        result.append(i.capitalize())
    return " ".join(result)

# Sum Mixed Array

def sum_mix(arr):
    x = 0
    for i in arr:
        x += int(i)
    
    return x

# Array plus array

# NO


# Reversed Words

def reverse_words(s):
    sArr = s.split()
    return " ".join(sArr[::-1])

# Sum The Strings

def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif a == "":
        return b
    elif b == "":
        return a
    else:
        return str(int(a) + int(b))

