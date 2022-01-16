from functools import reduce

def is_funny(s):
    return reduce(lambda x,y: x and y, [True if char == 'h' or char == 'a' else False for char in s])


print(is_funny("aaaaahhhh"))