# Regex count lowercase letters

def lowercase_count(strng):
    re = 0
    for i in strng:
        if i.islower():
            re += 1 
            
    
    return re

# Find the capitals

def capitals(word):
    indexes = []
    for i in range(len(word)):
        if word [i].isupper():
            indexes.append(i)
    return  indexes