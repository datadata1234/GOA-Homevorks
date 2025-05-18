# Printer Errors

def printer_error(s):
    errors = 0
    for i in s:
        if i > 'm':
            errors += 1
    return f"{errors}/{len(s)}"

# Don't give me five!

def dont_give_me_five(start, end):
    count = 0
    for num in range(start, end + 1):
        if '5' not in str(num):
            count += 1
    return count

# Triangular Treasure

def triangular(n):
    if n < 0:
        return 0
    return n * (n + 1) // 2

# Sorted? yes? no? how?

# NO

# Bumps in the Road

def bumps(road):
    
    bump_count = road.count('n')
    
    if bump_count <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"
    
