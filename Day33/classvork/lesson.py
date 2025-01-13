 # Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    return length * width * height

# Grasshopper - Array Mean
def find_average(nums):
    return sum(nums) / len(nums)

# Is he gonna survive?

def hero(bullets, dragons):
    return bullets >= dragons * 2

# Exes and Ohs

def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")

# No zeros for heros

def no_boring_zeros(n):
    if n == 0:
        return 0
        
    n = str(n)
    
    while n[-1] == "0":
        n = n[:-1]
        
    return int(n)

# Student's Final Grade

