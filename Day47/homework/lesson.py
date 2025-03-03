# 2)შეასრულეთ თქვენი არჩეული 3ცალი 8KYUანი ამოცანა

# Disemvowel Trolls

def disemvowel(string_):
    aeiou = "aeiou"
    for i in aeiou:
        string_ = string_.replace(i, "")
        string_ = string_.replace(i.upper(),"")
    return string_

# Convert a string to an array

def string_to_array(s):
    return s.split(' ')

# Sum of positive


def positive_sum(arr):
    result = 0
    for i in arr:
        if i > 0:
            result += i
            
    return result

# 3)შეასრულეთ თქვენი არჩეული 2ცალი 7KYUანი ამოცანა

# Highest and Lowest

def high_and_low(numbers):
    x = numbers.split()
    y = [int(i) for i in x]
    y.sort()
    numbers = str(y[-1]) + " " + str(y[0])
    return numbers

# Ones and Zeros
def binary_array_to_number(arr):
    return sum([arr[i] * (2 ** (len(arr) - i - 1)) for i in range(len(arr))])

# 4)შეასრულეთ თქვენი არჩეული 1ცალი 6KYUანი ამოცანა

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