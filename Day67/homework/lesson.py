# Jaden Casing Strings

def to_jaden_case(string):
    result = []
    string = string.split()
    for i in string:
        result.append(i.capitalize())
    return " ".join(result)

# Beginner Series #3 Sum of Numbers

def get_sum(a, b):
    if a == b:
        return a
    elif a < b:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))
    
# Maximum Length Difference

def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1

    max_diff = 0
    for x in a1:
        for y in a2:
            max_diff = max(max_diff, abs(len(x) - len(y)))
    return max_diff

# Simple beads count

def count_red_beads(n):
    if n < 2:
        return 0
    else:
        return 2 * (n - 1)
    
# Simple Fun #136: Missing Values

# NO
