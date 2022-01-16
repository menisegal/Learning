


from functools import reduce
import math


def is_prime(number):
    return reduce(lambda x,y: x and y, [True if number % i != 0 else False for i in range(2,math.floor(math.sqrt(number)))])


print(is_prime(42))
print(is_prime(43))
