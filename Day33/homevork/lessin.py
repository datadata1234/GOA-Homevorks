# You Can't Code Under Pressure #1

def double_integer(i):
    return i * 2

# Friend or Foe?


def friend(x):
    st = []
    for i in x:
        if len(i) == 4:
            st.append(i)
            
    return st   

# Beginner - Reduce but Grow

def grow(arr):
    st = 1
    for i in arr:
        st = st * i 
    return st

# Calculate average


def find_average(numbers):
    if numbers == [] or numbers == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)
    
# Grasshopper - Messi goals function

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# Double Char

def double_char(s):
    st = ""
    for i in s:
        st += i * 2
    return st 

# Remove anchor from URL

def remove_url_anchor(url):
    st = ""
    if "#" not in url:
        return url
    for i in url:
        if i != "#":
            st += i
        elif i == "#":
            return st
        
# Sum of Cubes

def sum_cubes(n):
    sum = 0 
    for i in range(1,n + 1):
        sum += i ** 3
    return sum



# Grasshopper - Messi goals function
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague