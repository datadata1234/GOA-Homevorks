# Credit Card Mask

def maskify(cc):
    st = ""
    l = []
    for i in cc [:-4]:
        l.append(i.replace(i, "#")) 
    st += cc[-4:]
    
    return "".join(l) + st

# String ends with?

def solution(text, ending):
    return text.endswith(ending)

# Sum of Cubes

def sum_cubes(n):
    sum = 0 
    for i in range(1,n + 1):
        sum += i ** 3
    return sum

# Sort Numbers

def solution(nums):
    if nums == None:
        return []
    else:
        return sorted(nums)
