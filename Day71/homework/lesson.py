# Who likes it?

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

# Create Phone Number

def create_phone_number(n):
    st = "("
    st += str(n[0])
    st += str(n[1])
    st += str(n[2])
    st += ") "
    
    st += str(n[3])
    st += str(n[4])
    st += str(n[5])
    st += "-"
    
    
    st += str(n[6])
    st += str(n[7])
    st += str(n[8])
    st += str(n[9])
    
    return st

# ძველი ამოხსნილია

# Find the odd int

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

# Row Weights

# NO

# Largest pair sum in array

def largest_pair_sum(numbers): 
    res = []
    x = max(numbers)
    numbers.remove(x)
    y = max(numbers)
    
    return x + y