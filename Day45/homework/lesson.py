# Dollars and Cents

def format_money(amount):
    return f"${amount:.2f}"

# Swap Values

#  NO

# Check same case

# NO

# Sum of Multiples

def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return "INVALID"
    return sum(range(n, m , n))

# Multiple of index

def multiple_of_index(arr):
    x = []
    
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            x.append(arr[i])
            
    if arr[0] == 0:
        x.insert(0,0)
        return x
    else:
        return x
    
# How old will I be in 2099?

def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age > 0:
        return f"You are {age} year{'s' if age > 1 else ''} old."
    elif age < 0:
        return f"You will be born in {abs(age)} year{'s' if abs(age) > 1 else ''}."
    else:
        return f"You were born this very year!"
