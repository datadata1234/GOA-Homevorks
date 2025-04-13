# The highest profit wins!

def min_max(lst):
    return [min(lst),max(lst)]

# Leap Years

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
    
# Fizz Buzz

def fizzbuzz(n):
    list1 = list(range(1,n+1))
    res = []

    for  i in list1:
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 ==0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(i)
    return res

# Simple Fun #136: Missing Values

# NO
