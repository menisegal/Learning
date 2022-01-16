from functools import reduce

def add(x,y):
    return x+y

def sum_of_digits(number):
    return reduce(add, list((str(number))))

print(sum_of_digits(104))