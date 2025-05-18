# Array.diff

def array_diff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    return result

# Duplicate Encoder

def duplicate_encode(word):
    word = word.lower()
    result = ''
    for char in word:
        if word.count(char) == 1:
            result += '('
        else:
            result += ')'
    return result

# Break camelCase

def solution(s):
    res = ""
    for i in s:
        if i != i.upper():
            res += i
        if i == i.upper():
            res += " " + i
    return res

# Are the numbers in order?

def in_asc_order(arr):
    if arr == sorted(arr):
        return True
    else:
        return False
    
# Remove duplicate words

# NO