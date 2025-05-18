# Printer Errors

def printer_error(s):
    errors = 0
    for i in s:
        if i > 'm':
            errors += 1
    return f"{errors}/{len(s)}"

# Printer Errors

def printer_error(s):
    errors = 0
    for i in s:
        if i > 'm':
            errors += 1
    return f"{errors}/{len(s)}"

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