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

# Categorize New Member

def open_or_senior(data):
    result = []
    
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
            
    return result



# 4) შექმენით manual_len ფუნქცია "ფუნქციაში არ უნდა გამოიყენოთ len()"

def manual_len(manual_list):
    count = 0

    for i in manual_list:
        count += 1
    return count

print(manual_len("data"))

