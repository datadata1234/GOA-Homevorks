# Remove First and Last Character Part Two

def array(string):
    if not string or string.count(",") < 2:
        return None
    chars = string.split(",") 
    three = chars[1:-1]
    if not three:
        return None
    return ' '.join(three)

# Template Strings

def temple_strings(obj, feature): 
    return obj + " are " + feature

# ontamination #1 -String-

def contamination(text, char):
    result = ""
    for i in text:
        result += char
    return result

# Is it a palindrome?

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# Email Address Obfuscator

# ვერ გავაკეთე