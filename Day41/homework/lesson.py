# ჯერ არ დამიწერია


# Grasshopper - Messi goals function

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# How good are you really?

def better_than_average(class_points, your_points):
    return sum(class_points) //  len(class_points) < your_points

# Volume of a Cuboid

def get_volume_of_cuboid(length, width, height):
    return length * width * height

# Sum without highest and lowest number

def sum_array(arr):
    if arr == None or arr == [] or len(arr) == 1:
        return 0
    else:
        return sum(arr) - min(arr) - max(arr)
    
# The Wide-Mouthed frog!

def mouth_size(animal): 
    animal = animal.lower()
    
    if animal == "alligator":
        return  "small"
    else:
        return "wide"
    

# გავიმრეორე ყველა მეთოდი 