# Isograms

def is_isogram(string):
    return len(set(string.lower())) == len(string.lower())

# Jaden Casing Strings

def to_jaden_case(string):
    result = []
    string = string.split()
    for i in string:
        result.append(i.capitalize())
    return " ".join(result)

# Regex validate PIN code

def validate_pin(pin):
    if pin.isdigit():
        if int(pin) >= 0:
            return  len(pin) == 4 or len(pin) == 6
    else:
        return False
    
# Mumbling

# NO

# Sum of odd numbers

def row_sum_odd_numbers(n):
    return n**3
