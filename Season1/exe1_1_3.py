

def is_divide(num):
    if num % 4 == 0:
        return num

def four_dividers(number):
    return list(filter(is_divide, range(1,number)))
    











print(four_dividers(9))
print(four_dividers(3))


