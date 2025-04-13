# Get the mean of an array

# NO

# Total amount of points

def points(games):
    result = 0
    
    for i in games:
        x = int(i[0])
        y = int(i[2])
        
        if x > y:
            result += 3
        elif x == y:
            result += 1
            
    return result

# Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted(numbers)[0] + sorted(numbers)[1]

# Number of People in the Bus

def number(bus_stops):  
    people_on_bus = 0
    for stop in bus_stops:       
        people_on = stop[0] 
        people_off = stop[1]
        people_on_bus += people_on - people_off
    return people_on_bus

# Build a square

# NO

# Multiples of 3 or 5

# NO