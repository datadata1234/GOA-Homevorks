# Printer Errors

def printer_error(s):
    errors = 0
    for i in s:
        if i > 'm':
            errors += 1
    return f"{errors}/{len(s)}"

# Number of People in the Bus

def number(bus_stops):  
    people_on_bus = 0
    for stop in bus_stops:       
        people_on = stop[0] 
        people_off = stop[1]
        people_on_bus += people_on - people_off
    return people_on_bus

# Don't give me five!

def dont_give_me_five(start, end):
    count = 0
    for num in range(start, end + 1):
        if '5' not in str(num):
            count += 1
    return count

# Array.diff

def array_diff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    return result

# Take a Ten Minutes Walk

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    if walk.count('n') != walk.count('s'):
        return False
    if walk.count('w') != walk.count('e'):
        return False
    return True

# Sum of Digits / Digital Root

def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Unique In Order

def unique_in_order(sequence):
    res = []
    res1 = ""
    for i in sequence:
        if i != res1:
            res.append(i)
            res1 = i
    return res 
