# Thinkful - Logic Drills: Traffic light

def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    
# Count by X

def count_by(x, n):
    result = []
    
    for i in range(1, n + 1):
        result.append(x * i) 
    return result
    
# Abbreviate a Two Word Name

# NO

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

# Jenny's secret message

def greet(name):
    if name != "Johnny":
        return f"Hello, {name}!".format(name = name)
    else:
        return "Hello, my love!"
    































