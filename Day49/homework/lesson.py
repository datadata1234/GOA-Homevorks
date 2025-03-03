# Unfinished Loop - Bug Fixing #1

def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1
    return res

# Return the day

def whatday(num):
    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"
    
# Take the Derivative

def derive(coefficient, exponent): 
    return f"{coefficient * exponent}x^{exponent - 1 }"

# Leap Years

# NO

# For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre

def quote(fighter):
    if fighter.lower() == "conor mcgregor":
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return "I am not impressed by your performance."
    