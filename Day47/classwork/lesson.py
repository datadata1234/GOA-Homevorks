# Expressions Matter

# NO

# String array duplicates

def dup(arry):
    st = []
    for i in arry:
        new_st = []
        for s in i:
            if not new_st or new_st[-1] != s:
                new_st.append(s)
        st.append(''.join(new_st))
        
    return st

# Stop gninnipS My sdroW!

def spin_words(sentence):
    arr = sentence.split()
    ddd = []
    for i in arr:
        if len(i) >= 5:
            ddd.append(i[::-1])
        else:
            ddd.append(i)
    return " ".join(ddd)

# Fix string case

def solve(s):
    upper = 0
    lower = 0
    
    for char in s:
        if char.islower():
            lower += 1
        else:
            upper += 1
            
    if upper == lower or lower > upper:
        return s.lower()
    else:
        return s.upper()
    
# Form The Minimum

def min_value(digits):
    no_duplicates = []
    
    for i in digits:
        if i not in no_duplicates:
            no_duplicates.append(i)
    
    result = ""
    
    for i in sorted(no_duplicates):
        result += str(i)
    return int(result)

# Maximum Multiple

def max_multiple(divisor, bound):
    #your code here
    word = []
    for d in range(1, bound + 1):
        if d % divisor == 0:
            word.append(d)
            
    return max(word)

# Case-sensitive!

# NO