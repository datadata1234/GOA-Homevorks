# List Filtering

def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result

# Exes and Ohs

def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")

# Shortest Word

def find_short(s):   
    words = s.split()    
    shortest_length = min(len(word) for word in words)
    return shortest_length

# Friend or Foe?

def friend(x):
    st = []
    for i in x:
        if len(i) == 4:
            st.append(i)
            
    return st  

# Two to One

def longest(a1, a2):
    result = set(a1 + a2)
    list1 = "".join(sorted(result)) 
    return list1