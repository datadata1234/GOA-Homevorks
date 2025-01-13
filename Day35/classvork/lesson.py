# Find the capitals

def capitals(word):
    indexes = []
    for i in range(len(word)):
        if word [i].isupper():
            indexes.append(i)
    return  indexes

# Maximum Multiple

def max_multiple(divisor, bound):
    word = []
    for d in range(1, bound + 1):
        if d % divisor == 0:
            word.append(d)
            
    return max(word)

# Summing a number's digits

# ვერ გავაკეთე



# Sum without highest and lowest number

def sum_array(arr):
    if arr == None or arr == [] or len(arr) == 1:
        return 0
    else:
        return sum(arr) - min(arr) - max(arr)