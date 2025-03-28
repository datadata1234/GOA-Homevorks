# Remove duplicates from list

def distinct(seq):   
    result = []
    
    for i in seq:
        if i not in result:
            result.append(i)
            
    return result

# Get Planet Name By ID

def get_planet_name(id):

    switch = {
         1: "Mercury",
         2: "Venus",
         3:  "Earth",
         4:  "Mars",
         5:  "Jupiter",
         6:  "Saturn",
         7:  "Uranus",
         8: "Neptune",
    }
    
    return switch[id]

# Switch it Up!

def switch_it_up(number):
    number_to_word = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

    return number_to_word[number]

# 5 without numbers !!

def unusual_five():
    return len(".....")