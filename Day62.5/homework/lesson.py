# Largest pair sum in array


def largest_pair_sum(numbers): 
    res = []
    x = max(numbers)
    numbers.remove(x)
    y = max(numbers)
    
    return x + y

# Reverse words

def reverse_words(text):
    text = text.split(" ")
    res = ""
    for i in text:
        res += " " + i[::-1]
    
    return res[1:]

# Reverse words

def reverse_words(text):
    text = text.split(" ")
    res = ""
    for i in text:
        res += " " + i[::-1]
    
    return res[1:]
