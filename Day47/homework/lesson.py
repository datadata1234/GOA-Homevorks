# 8 kyu



# Template Strings

def temple_strings(obj, feature): 
    return obj + " are " + feature

# Sum The Strings

def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif a == "":
        return b
    elif b == "":
        return a
    else:
        return str(int(a) + int(b))
    
# Keep Hydrated!

def litres(time):
    return time * 0.5 // 1



# 7 kyu



# Exes and Ohs


def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")

# tring ends with?

def solution(text, ending):
    # your code here...
    pass
    return text.endswith(ending)



# 6 kyu


# Counting Duplicates

def duplicate_count(text):
    x = []
    a = []
    s = 0
    for i in text:
        if i.lower() not in x:
            x.append(i.lower())
        else:
            if i.lower() not in a:
                s += 1
                a.append(i.lower())
    return s